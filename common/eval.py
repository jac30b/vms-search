from distutils.log import Log
from typing import *
from common.logger import Logger
from common.files import FileHelper
from vms.vms import Vectorizer
import json
from termcolor import colored


class EvalError(Exception):
    pass


class Eval:
    def __init__(self) -> None:
        self.logger = Logger.get_logger(__name__, "evaluator.log", "EVALUATOR", True)

    def preprocess(self, files: List[str]) -> bool:
        """
        Function that calls the Vectorizer responsible for preprocessing

        Args:
            files (List[str]): List of files that will be preprocessed

        Returns:
            bool: informs if preprocessed been done correctly
        """
        self.logger.debug(f"Preprocessing for files {files}")
        try:
            self.vectorizer = Vectorizer(files)
        except FileNotFoundError:
            return False
        return True

    def evaluate(self, req: str):
        """
        Evaluates the request from the repl

        Args:
            req (str): json represting the user request: {command: <>, content: <>}
            command is the action that has to be done
            content can be either files or query
        """
        request = json.loads(req)
        if request["command"] == "search":
            self.search(request["content"])
        elif request["command"] == "load":
            self.load_files(request["content"])

    def search(self, query: str) -> None:
        """
        Uses Vectorizer class to find the query in files

        Args:
            query (str): searched phrase
        """
        evaluated = self.vectorizer.process_query(query)
        print(colored(f"The best match is in the following doc: {evaluated}", "green"))

    def load_files(self, files: str) -> None:
        """
        Function parsing files from repl and starts the preprocessing

        Args:
            files (str): files requested by the user
        """
        files_parsed = FileHelper.parse_files(files)
        self.preprocess(files_parsed)
