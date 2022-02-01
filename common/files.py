from typing import *
from enum import Enum
import re
import os.path as op
from common.logger import Logger


class FileType(Enum):
    WEB_RESOURCE = 0
    FILE = 1


class FileHelper:
    def __init__(self):
        self.logger = Logger.get_logger(
            __name__, "file_helper.log", "FILE HELPER", True
        )

    """
    Class that provides functions useful to work with files
    """

    def process_files(self, files: List[str]) -> Dict[str, list]:
        """

        :param files:
        :return:
        """
        content = {}
        for path in files:
            f_type = FileHelper.resolve_path(path)
            if f_type == FileType.WEB_RESOURCE:
                self.logger.debug(f"Received web resource: {path}")
            elif f_type == FileType.FILE:
                self.logger.debug(f"Received file: {path}")
                if self.check_for_file(path):
                    ext = op.splitext(path)[1]
                    if ext not in [".txt", ".doc", ".docx", ".log"]:
                        self.logger.debug(f"Unsupported file extension: {path}")
                        continue
                    else:
                        file_content = open(path).readlines()
                        content[path] = file_content
                else:
                    continue
        return content

    @staticmethod
    def resolve_path(path: str) -> FileType:
        """

        :param path:
        :return:
        """
        if re.search(r"^http://|^https://", path):
            return FileType.WEB_RESOURCE
        else:
            return FileType.FILE

    def check_for_file(self, path: str) -> bool:
        """

        :param path:
        :return:
        """
        if op.exists(path):
            if op.isfile(path):
                return True
            else:
                self.logger.debug(f"Specified file is directory: {path}")
                return False
        else:
            self.logger.debug(f"File doesn't exist: {path}")
            return False


f = FileHelper()
print(f.process_files(["../logs/file_helper.log"]))
