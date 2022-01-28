import sys
import logging
import pathlib
import os.path


class Logger:
    """ """

    @staticmethod
    def get_logger(
        name: str, file: str, module_name: str, write_stdout: bool
    ) -> logging.Logger:
        """

        :param name:

        :param file:
        :param module_name:
        :return:
        """
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        pwd = pathlib.Path().resolve()
        if os.path.isdir("logs"):
            file_handler = logging.FileHandler("./logs/" + file)
        else:
            file_handler = logging.FileHandler("../logs/" + file)
        formatter = logging.Formatter(f"[{module_name}] %(asctime)s: %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        if write_stdout:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
        return logger
