from common.logger import Logger
from common.cli import CLI
from common.eval import Eval
from common.repl import REPL


def main():
    print("Please note that this app works only with English documents")
    args = CLI.parse()
    evaluator = Eval()
    if args.files:
        done = evaluator.preprocess(args.files)
    else:
        print("You must specify some files")
        return
    REPL.run_repl()


if __name__ == "__main__":
    if done:
        REPL.run_repl()
    else:
        print("Ops, there was some error while preprocessing files")
