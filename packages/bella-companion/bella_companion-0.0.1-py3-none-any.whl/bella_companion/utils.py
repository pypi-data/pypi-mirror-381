import os
import re
import subprocess
from glob import glob
from pathlib import Path
from typing import Any

import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import polars as pl
from joblib import Parallel, delayed
from lumiere.backend.typings import Weights
from tqdm import tqdm


def run_sbatch(
    command: str,
    log_dir: Path,
    time: str = "240:00:00",
    mem_per_cpu: str = "2000",
    overwrite: bool = False,
) -> str | None:
    if not overwrite and log_dir.exists():
        print(f"Log directory {log_dir} already exists. Skipping.")
        return
    cmd = " ".join(
        [
            "sbatch",
            f"-J {log_dir}",
            f"-o {log_dir / 'output.out'}",
            f"-e {log_dir / 'error.err'}",
            f"--time {time}",
            f"--mem-per-cpu={mem_per_cpu}",
            f"--wrap='{command}'",
        ]
    )
    output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    job_id = re.search(r"Submitted batch job (\d+)", output.stdout)
    if job_id is None:
        raise RuntimeError(
            f"Failed to submit job.\nCommand: {cmd}\nOutput: {output.stdout}\nError: {output.stderr}"
        )
    return job_id.group(1)


def get_job_metadata(job_id: str):
    output = subprocess.run(
        f"myjobs -j {job_id}", shell=True, capture_output=True, text=True
    ).stdout

    status = re.search(r"Status\s+:\s+(\w+)", output)
    if status is None:
        raise RuntimeError(f"Failed to get job status for job {job_id}")
    status = status.group(1)

    wall_clock = re.search(r"Wall-clock\s+:\s+([\d\-:]+)", output)
    if wall_clock is None:
        raise RuntimeError(f"Failed to get wall-clock time for job {job_id}")
    wall_clock = wall_clock.group(1)

    if "-" in wall_clock:
        days, wall_clock = wall_clock.split("-")
        days = int(days)
    else:
        days = 0
    hours, minutes, seconds = map(int, wall_clock.split(":"))
    total_hours = days * 24 + hours + minutes / 60 + seconds / 3600

    return {"status": status, "total_hours": total_hours}


def summarize_log(
    log_file: str,
    target_columns: list[str],
    burn_in: float = 0.1,
    hdi_prob: float = 0.95,
    hidden_nodes: list[int] | None = None,
    n_weights_samples: int = 100,
    n_features: dict[str, int] | None = None,
    job_id: str | None = None,
) -> tuple[dict[str, Any], dict[str, list[Weights]] | None]:
    df = pl.read_csv(log_file, separator="\t", comment_prefix="#")
    df = df.filter(pl.col("Sample") > burn_in * len(df))
    targets_df = df.select(target_columns)
    summary: dict[str, Any] = {"n_samples": len(df)}
    for column in targets_df.columns:
        summary[f"{column}_median"] = targets_df[column].median()
        summary[f"{column}_ess"] = az.ess(  # pyright: ignore[reportUnknownMemberType]
            np.array(targets_df[column])
        )
        lower, upper = az.hdi(  # pyright: ignore[reportUnknownMemberType]
            np.array(targets_df[column]), hdi_prob=hdi_prob
        )
        summary[f"{column}_lower"] = lower
        summary[f"{column}_upper"] = upper
    if job_id is not None:
        summary.update(get_job_metadata(job_id))
    if hidden_nodes is not None:
        if n_features is None:
            raise ValueError("`n_features` must be provided to summarize log weights.")
        weights: dict[str, list[Weights]] = {}
        for target, n in n_features.items():
            nodes = [n, *hidden_nodes, 1]
            layer_weights = [
                np.array(
                    df.tail(n_weights_samples).select(
                        c for c in df.columns if c.startswith(f"{target}W.{i}")
                    )
                ).reshape(-1, n_inputs + 1, n_outputs)
                for i, (n_inputs, n_outputs) in enumerate(zip(nodes[:-1], nodes[1:]))
            ]
            weights[target] = [
                list(sample_weights) for sample_weights in zip(*layer_weights)
            ]
        return summary, weights
    return summary, None


def summarize_logs(
    logs_dir: Path,
    target_columns: list[str],
    burn_in: float = 0.1,
    hdi_prob: float = 0.95,
    hidden_nodes: list[int] | None = None,
    n_weights_samples: int = 100,
    n_features: dict[str, int] | None = None,
    job_ids: dict[str, str] | None = None,
) -> tuple[pl.DataFrame, dict[str, list[list[Weights]]] | None]:
    def _get_log_summary(
        log_file: str,
    ) -> tuple[dict[str, Any], dict[str, list[Weights]] | None]:
        log_id = Path(log_file).stem
        summary, weights = summarize_log(
            log_file=log_file,
            target_columns=target_columns,
            burn_in=burn_in,
            hdi_prob=hdi_prob,
            hidden_nodes=hidden_nodes,
            n_weights_samples=n_weights_samples,
            n_features=n_features,
            job_id=job_ids[log_id] if job_ids is not None else None,
        )
        return {"id": log_id, **summary}, weights

    os.environ["POLARS_MAX_THREADS"] = "1"
    summaries = Parallel(n_jobs=-1)(
        delayed(_get_log_summary)(log_file)
        for log_file in tqdm(glob(str(logs_dir / "*.log")))
    )
    data, weights = zip(*summaries)
    if any(w is not None for w in weights):
        assert n_features is not None
        return pl.DataFrame(data), {t: [w[t] for w in weights] for t in n_features}
    return pl.DataFrame(data), None


def set_plt_rcparams():
    plt.rcParams["pdf.fonttype"] = 42
    plt.rcParams["xtick.labelsize"] = 14
    plt.rcParams["ytick.labelsize"] = 14
    plt.rcParams["font.size"] = 14
    plt.rcParams["figure.constrained_layout.use"] = True
    plt.rcParams["lines.linewidth"] = 3
