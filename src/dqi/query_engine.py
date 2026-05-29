from collections import defaultdict
from typing import List, Tuple

from .index_manager import InvertedIndex, _tokenize


class QueryEngine:
    """Simple query engine using TF-IDF ranking over an InvertedIndex."""

    def __init__(self, index: InvertedIndex):
        self.index = index

    def search(self, query: str, top_n: int = 10) -> List[Tuple[str, float]]:
        terms = _tokenize(query)
        if not terms:
            return []

        scores = defaultdict(float)
        for term in terms:
            postings = self.index.get_postings(term)
            idf = self.index.idf(term)
            for doc_id, tf in postings.items():
                scores[doc_id] += tf * idf

        results = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return results[:top_n]
