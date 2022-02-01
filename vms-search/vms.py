from os import stat
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys

sys.path.insert(0, "/Users/joker/Documents/fun/vms-search")
from common.files import FileHelper

# from common.cache import Cache
from common.tokenizer import Tokenizer
from typing import *


class Vectorizer:
    def __init__(self, files) -> None:
        # file_helper = FileHelper()
        # self.documents = file_helper.process_files(files)
        self.documents = {
            "/home/tmp": """At eight o'clock on Thursday morning Arthur didn't feel very good.""",
            "test": "TEST TEST test",
        }
        tokenizer = Tokenizer()
        vectorizer = TfidfVectorizer(
            tokenizer=tokenizer.tokenize_and_stem, stop_words="english"
        )
        body = list(self.documents.values())
        vectorizer.fit(body)
        self.document_vector = vectorizer.transform(body)
        self.vectorizer = vectorizer

    def process_query(self, query):
        query_vector = self.vectorizer.transform([query]).todense()
        cos_sim = cosine_similarity(query_vector, self.document_vector)
        ranks = (-cos_sim).argsort(axis=None)
        return list(self.documents.keys())[ranks[0]]


tmp = Vectorizer(["test"])
print(tmp.process_query(""))
