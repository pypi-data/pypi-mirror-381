import argparse

from dotenv import load_dotenv


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(prog="bella")
    subparsers = parser.add_subparsers(dest="command")

    gen_sim_data_parser = subparsers.add_parser("generate-simulations-data")
    generate_simulations_data_parser.set_defaults(func=generate_simulations_data)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


def generate_simulations_data(args):
    print("Generating simulations data...")
    # your logic here
