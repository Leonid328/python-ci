# Flask Product API

Simple Flask API for products (CRUD).

## Setup

```bash
pip install -r requirements.txt
python db.py -a
python app.py --host localhost --port 5000
```

Tests: `pytest`

CI: `.github/workflows/ci.yml`

CI runs on pull_request (opened / synchronize) and on workflow_dispatch.
