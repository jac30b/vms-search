from distutils.log import Log
from typing import *
from common.logger import Logger
import json


class EvalError(Exception):
    pass


class Eval:
    def __init__(self) -> None:
        self.logger = Logger.get_logger(__name__, "evalutaor.log", "EVALUATOR", True)

    def preprocess(self, files: List[str]) -> bool:
        self.logger.debug(f"Preprocessing for files {files}")
        return True

    def evaluate(self, req):
        print(json.loads(req))
        pass
