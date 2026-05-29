import math
from collections import defaultdict
from typing import Dict, Iterable


def _tokenize(text: str):
    return [t for t in text.lower().split() if t]


class InvertedIndex:
    """Memory-efficient inverted index with basic TF-IDF support."""

    def __init__(self):
        self._postings: Dict[str, Dict[str, int]] = defaultdict(dict)
        self._doc_lengths: Dict[str, int] = {}
        self._doc_count = 0

    def add_document(self, doc_id: str, text: str) -> None:
        terms = _tokenize(text)
        if not terms:
            return
        counts = defaultdict(int)
        for t in terms:
            counts[t] += 1
        for term, freq in counts.items():
            self._postings[term][doc_id] = freq
        self._doc_lengths[doc_id] = len(terms)
        self._doc_count = len(self._doc_lengths)

    def remove_document(self, doc_id: str) -> None:
        for term in list(self._postings.keys()):
            self._postings[term].pop(doc_id, None)
            if not self._postings[term]:
                del self._postings[term]
        self._doc_lengths.pop(doc_id, None)
        self._doc_count = len(self._doc_lengths)

    def get_postings(self, term: str) -> Dict[str, int]:
        return self._postings.get(term, {})

    def idf(self, term: str) -> float:
        df = len(self._postings.get(term, {}))
        if df == 0:
            return 0.0
        return math.log((self._doc_count + 1) / df)

    def documents(self) -> Iterable[str]:
        return list(self._doc_lengths.keys())
