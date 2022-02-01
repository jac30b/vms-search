from matplotlib.style import available
from common.logger import Logger
import json


available_commands = ["search"]


class QueryError(Exception):
    pass


class Query:
    def __init__(self) -> None:
        self.logger = Logger.get_logger(__name__, "parser.log", "PARESER", False)

    def parse_repl(self, query):
        self.logger.debug(f"Parsing query: {query}")
        command = query.split()[0]
        if command not in available_commands:
            self.logger.debug(f"Command doesn't exist: {command}")
            raise QueryError(f"Command '{command}' not found")

        return json.dumps({"command": command, "query": " ".join(query.split()[1:])})
