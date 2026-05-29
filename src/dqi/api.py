from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .storage import Storage
from .index_manager import InvertedIndex
from .query_engine import QueryEngine

app = FastAPI(title="dqi")
store = Storage()
index = InvertedIndex()
engine = QueryEngine(index)


class DocIn(BaseModel):
    id: str | None = None
    text: str


@app.post("/doc")
def add_doc(doc: DocIn):
    doc_id = store.add_document(doc.text, doc.id)
    index.add_document(doc_id, doc.text)
    return {"id": doc_id}


@app.get("/doc/{doc_id}")
def get_doc(doc_id: str):
    doc = store.get_document(doc_id)
    if doc is None:
        raise HTTPException(status_code=404, detail="not found")
    return {"id": doc_id, "text": doc}


@app.get("/search")
def search(q: str, n: int = 10):
    results = engine.search(q, top_n=n)
    return [{"id": doc_id, "score": score} for doc_id, score in results]
