import json
import os

import joblib

from src.config import BEAST_LOGS_SUMMARIES_DIR, BEAST_OUTPUTS_DIR
from src.simulations.scenarios import SCENARIOS
from src.utils import summarize_logs


def main():
    with open(BEAST_OUTPUTS_DIR / "simulations_job_ids.json", "r") as f:
        job_ids: dict[str, dict[str, dict[str, str]]] = json.load(f)

    for scenario_name, scenario in SCENARIOS.items():
        summaries_dir = BEAST_LOGS_SUMMARIES_DIR / scenario_name
        os.makedirs(summaries_dir, exist_ok=True)
        for model in job_ids[scenario_name]:
            hidden_nodes = (
                list(map(int, model.split("-")[1].split("_")))
                if model.startswith("MLP")
                else None
            )
            logs_dir = BEAST_OUTPUTS_DIR / scenario_name / model
            print(f"Summarizing {scenario_name} - {model}")
            logs_summary, weights = summarize_logs(
                logs_dir,
                target_columns=[c for t in scenario.targets.values() for c in t],
                hidden_nodes=hidden_nodes,
                n_features={t: len(fs) for t, fs in scenario.features.items()},
                job_ids=job_ids[scenario_name][model],
            )
            logs_summary.write_csv(summaries_dir / f"{model}.csv")
            if weights is not None:
                joblib.dump(weights, summaries_dir / f"{model}.weights.pkl")


if __name__ == "__main__":
    main()
