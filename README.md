# Distributed Query & Index System

A systems-oriented backend project focused on indexing and query optimization.

## Why This Repo Matters

This is the strongest system-design-oriented repo in your resume.
It should demonstrate:

- architecture thinking
- scalability awareness
- indexing concepts
- abstraction design

## Planned Components

- Query parser
- Index manager
- Storage engine
- Benchmark scripts
- API layer

## Important Rule

Do NOT overclaim distributed systems experience.
Keep implementation honest and educational.

## Suggested Deliverables

- benchmark results
- architecture diagrams
- query complexity notes
- design tradeoff documentation

Getting started
--------------

Run the FastAPI app locally:

```bash
pip install -r requirements.txt
python -m src
```

Add documents via POST `/doc` and query with GET `/search?q=...`.

Project layout
--------------

- `src/dqi/` - package containing `storage`, `index_manager`, `query_engine`, and `api`.
- `tests/` - pytest-based unit tests.
