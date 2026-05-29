from typing import Dict, Optional


class Storage:
    """Simple in-memory document store.

    Suitable for testing and local development. Thread-safe usage is left to callers.
    """

    def __init__(self):
        self._docs: Dict[str, str] = {}
        self._next_id = 1

    def add_document(self, text: str, doc_id: Optional[str] = None) -> str:
        if doc_id is None:
            doc_id = str(self._next_id)
            self._next_id += 1
        self._docs[doc_id] = text
        return doc_id

    def get_document(self, doc_id: str) -> Optional[str]:
        return self._docs.get(doc_id)

    def delete_document(self, doc_id: str) -> bool:
        return self._docs.pop(doc_id, None) is not None

    def all_documents(self):
        return self._docs.items()
