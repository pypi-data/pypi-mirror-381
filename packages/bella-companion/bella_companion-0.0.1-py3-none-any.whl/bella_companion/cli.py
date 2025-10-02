import argparse

from dotenv import load_dotenv
from bella_companion.simulations import generate_data


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        prog="bella",
        description="Companion tool with experiments and evaluation for Bayesian Evolutionary Layered Learning Architectures (BELLA) BEAST2 package.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    gen_sim_data_parser = subparsers.add_parser(
        "generate-simulations-data", help="Generate simulation data"
    )
    gen_sim_data_parser.set_defaults(func=generate_data)

    args = parser.parse_args()
    args.func()
