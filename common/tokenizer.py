from typing import *
import nltk
import string

class Tokenizer:
    def __init__(self) -> None:
        pass

    def tokenize(self, words: Dict[str, str]) -> Dict[str, Dict[str, int]]:
        """
        Function that splits the text into words and remove a punctuation marks.
        """
        punct_table = str.maketrans({x: None for x in string.punctuation})
        tokenized = {}
        for file, text in words:
            tokenized[file] = nltk.word_tokenize(text.translate(punct_table))
        return tokenized

    def stem(self, words: Dict[str, str]) -> Dict[str, Dict[str, int]]:
        """
        Function that remove stop words, lower words and strip words of their plural forms
        """
        pass

