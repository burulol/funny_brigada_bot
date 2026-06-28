import json
from pathlib import Path

FILE = Path("count.json")

def increment_count(user_id):
    d = load_count()
    d[user_id] = d.get(user_id, 0) + 1
    save(d)

def save(d: dict):
    FILE.write_text(json.dumps(d, indent=2))

def load_count() -> dict:
    return json.loads(FILE.read_text()) if FILE.exists() else {}

def update(new: dict):
    d = load_count()
    d.update(new)
    save(d)