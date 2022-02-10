from typing import *
from common.query import Query, QueryError
from common.eval import Eval, EvalError
from termcolor import colored


class REPL:
    @staticmethod
    def run_repl() -> None:
        """
        Function that runs interactive terminal for the user. 
        """
        pareser = Query()
        evaluator = Eval()
        try:
            while True:
                try:
                    _input = input("$ ")
                    parsed = pareser.parse_repl(_input)
                    evaluator.evaluate(parsed)
                except QueryError as e:
                    print(colored(e, "red"))
                except EvalError as e:
                    print(colored(e, "red"))
        except KeyboardInterrupt:
            print("\nClosing repl....")
