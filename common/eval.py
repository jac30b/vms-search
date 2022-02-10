from distutils.log import Log
from typing import *
from common.logger import Logger
from common.files import FileHelper
from vms.vms import Vectorizer
import json


class EvalError(Exception):
    pass


class Eval:
    def __init__(self) -> None:
        self.logger = Logger.get_logger(__name__, "evaluator.log", "EVALUATOR", True)

    def preprocess(self, files: List[str]) -> bool:
        self.logger.debug(f"Preprocessing for files {files}")
        try:
            self.vectorizer = Vectorizer(files)
        except FileNotFoundError:
            return False
        return True


    def evaluate(self, req):
        request = json.loads(req)
        if request['command'] == "search":
            self.search(request['content'])
        elif request['command'] == "load":
            self.load_files(request['content'])

    def search(self, query):
        result = self.vectorizer.process_query(query)
        print(result)

    def load_files(self, files):
        files_parsed = FileHelper.parse_files(files)
        self.preprocess(files_parsed)
