import argparse

from ab.gpt.util.AlterNN import alter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--epochs', type=int, default=8, help="Maximum number of generation epochs.")
    parser.add_argument('-n', '--num-supporting-models', type=int, default=1, help="Number of supporting models to fetch from database for more ideas.")
    args = parser.parse_args()
    alter(args.epochs, 'NN_alter.json', 'deepseek-ai/DeepSeek-R1-Distill-Qwen-7B', n=args.num_supporting_models)


if __name__ == "__main__":
    main()
