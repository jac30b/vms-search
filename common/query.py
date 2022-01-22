from logger import Logger
from typing import *


class Query:
    def __init__(self):
        self.logger = Logger.get_logger(__name__, 'query.log', 'QUERY')

    def parse(self, query: str):
        pass

    def validate_query(self, query: str) -> bool:
        pass
