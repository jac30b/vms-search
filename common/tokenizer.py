from common.logger import Logger
from typing import *
import nltk
from nltk.stem import PorterStemmer
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download("punkt")
import string


class Tokenizer:
    def __init__(self) -> None:
        self.logger = Logger.get_logger(__name__, "tokenizer.log", "TOKOK", False)

    def tokenize(self, words: List[str]) -> List[str]:
        """
        Function that splits the text into words and remove a punctuation marks.
        """
        self.logger.debug(f"Tokenizing detected")
        punct_table = str.maketrans({x: None for x in string.punctuation})
        tokenized = {}
        tokenized = nltk.word_tokenize(words.translate(punct_table))
        return tokenized

    def stem(self, words: List[str]) -> List[str]:
        """
        Function that remove stop words, lower words and strip words of their plural forms
        """
        self.logger.debug(f"Stemming detected")
        porter_stemmer = PorterStemmer()
        words = [porter_stemmer.stem(word) for word in words]
        return words

    def tokenize_and_stem(self, words: Dict[str, str]) -> Dict[str, List[str]]:
        toknized = self.tokenize(words)
        return self.stem(toknized)
