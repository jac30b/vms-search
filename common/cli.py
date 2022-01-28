import argparse


class CLI:
    @staticmethod
    def parse() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(description="Search through your documents")
        # TODO: Add support for dir
        parser.add_argument("files", nargs="*", help="Files that you want to search")

        args = parser.parse_args()
        return args
