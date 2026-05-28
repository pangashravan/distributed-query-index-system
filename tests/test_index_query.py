from dqi.storage import Storage
from dqi.index_manager import InvertedIndex
from dqi.query_engine import QueryEngine


def test_basic_index_search():
    s = Storage()
    idx = InvertedIndex()
    qe = QueryEngine(idx)

    id1 = s.add_document("The quick brown fox")
    id2 = s.add_document("Quick brown dogs")

    idx.add_document(id1, s.get_document(id1))
    idx.add_document(id2, s.get_document(id2))

    res = qe.search("quick brown")
    assert res
    assert res[0][0] in {id1, id2}
