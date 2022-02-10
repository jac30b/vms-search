from curses import resetty
from functools import cache
from os import stat
from matplotlib.pyplot import pink
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys

sys.path.insert(0, "/Users/joker/Documents/fun/vms-search")
from common.files import FileHelper
from common.cache import Cache

# from common.cache import Cache
from common.tokenizer import Tokenizer
from typing import *
import warnings
warnings.filterwarnings("ignore")


class Vectorizer:
    def __init__(self, files) -> None:
        self.cache = Cache(500)
        file_helper = FileHelper()
        self.documents = file_helper.process_files(files)
        tokenizer = Tokenizer()
        self.vectorizer = TfidfVectorizer(
            tokenizer=tokenizer.tokenize_and_stem, stop_words="english"
        )
        body = list(self.documents.values())
        self.vectorizer.fit(body)
        self.document_vector = self.vectorizer.transform(body)

    def process_query(self, query):
        cache_hit = self.cache.get(query)
        if cache_hit != -1:
            return cache_hit
        query_vector = self.vectorizer.transform([query]).todense()
        cos_sim = cosine_similarity(query_vector, self.document_vector)
        print(f'Cosine similarity: {cos_sim}')
        ranks = (-cos_sim).argsort(axis=None)
        result = list(self.documents.keys())[ranks[0]]
        self.cache.put(query, result)
        return result
