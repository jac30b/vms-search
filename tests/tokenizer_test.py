# TODO: Pack into modules
import sys

sys.path.insert(0, "/Users/joker/Documents/fun/vms-search")
import pytest
from common.tokenizer import Tokenizer

example_document = {
    "test": """At eight o'clock on Thursday morning Arthur didn't feel very good."""
}


class TokenizerTest:
    def __init__(self) -> None:
        self.tokenizer = Tokenizer()

    def test_output(self):
        print(self.tokenizer.tokenize(example_document))
