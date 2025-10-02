import json
import os
from collections import defaultdict
from glob import glob
from pathlib import Path

from numpy.random import default_rng
from phylogenie import Tree, load_newick
from phylogenie.utils import get_node_depths
from tqdm import tqdm

import config as cfg
from bella_companion.simulations.scenarios import SCENARIOS, ScenarioType
from bella_companion.utils import run_sbatch


def main():
    rng = default_rng(42)
    job_ids = {}
    for scenario_name, scenario in SCENARIOS.items():
        job_ids[scenario_name] = defaultdict(dict)
        data_dir = cfg.SIMULATED_DATA_DIR / scenario_name
        inference_configs_dir = (
            scenario_name.split("_")[0] if "_" in scenario_name else scenario_name
        )
        for tree_file in tqdm(
            glob(str(data_dir / "*.nwk")),
            desc=f"Submitting BEAST2 jobs for {scenario_name}",
        ):
            tree_id = Path(tree_file).stem
            for model in ["Nonparametric", "GLM"] + [
                f"MLP-{hidden_nodes}" for hidden_nodes in ["3_2", "16_8", "32_16"]
            ]:
                outputs_dir = cfg.BEAST_OUTPUTS_DIR / scenario_name / model
                os.makedirs(outputs_dir, exist_ok=True)
                beast_args = [
                    f"-D treeFile={tree_file},treeID={tree_id}",
                    f"-prefix {outputs_dir}{os.sep}",
                ]
                beast_args.extend(
                    [
                        f'-D {key}="{value}"'
                        for key, value in scenario.beast_args.items()
                    ]
                )
                beast_args.append(
                    f'-D randomPredictor="{" ".join(map(str, scenario.get_random_predictor(rng)))}"'
                )
                if scenario.type == ScenarioType.EPI:
                    tree = load_newick(tree_file)
                    assert isinstance(tree, Tree)
                    beast_args.append(
                        f"-D lastSampleTime={max(get_node_depths(tree).values())}"
                    )

                if model in ["Nonparametric", "GLM"]:
                    command = " ".join(
                        [
                            cfg.RUN_BEAST,
                            *beast_args,
                            str(
                                cfg.BEAST_CONFIGS_DIR
                                / inference_configs_dir
                                / f"{model}.xml"
                            ),
                        ]
                    )
                else:
                    nodes = model.split("-")[1].split("_")
                    command = " ".join(
                        [
                            cfg.RUN_BEAST,
                            *beast_args,
                            f'-D nodes="{" ".join(map(str, nodes))}"',
                            str(
                                cfg.BEAST_CONFIGS_DIR
                                / inference_configs_dir
                                / "MLP.xml"
                            ),
                        ]
                    )

                job_ids[scenario_name][model][tree_id] = run_sbatch(
                    command, cfg.SBATCH_LOGS_DIR / scenario_name / model / tree_id
                )

    with open(cfg.BEAST_OUTPUTS_DIR / "simulations_job_ids.json", "w") as f:
        json.dump(job_ids, f)


if __name__ == "__main__":
    main()
