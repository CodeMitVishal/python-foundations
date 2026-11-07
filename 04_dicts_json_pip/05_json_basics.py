"""Module 4 · Reading JSON

JSON is a text format for data, used in files and by web APIs. Python's
json module turns JSON text into dictionaries and lists, and back again.

Run it:  python 04_dicts_json_pip/05_json_basics.py
"""

import json
from pathlib import Path

# This looks like a dictionary, but the outer quotes make it just a str
text = '{"name": "Vishal", "langs": ["Python", "SQL"]}'
data = json.loads(text)       # str -> dict ("loads" = load from a string)
print(data["langs"][0])       # Python

back = json.dumps(data)       # dict -> str ("dumps" = dump to a string)
print(back)

# Read the JSON file that sits next to this script.
# Path(__file__).parent is this script's folder, so it works from anywhere.
json_file = Path(__file__).parent / "contacts.json"
# with open() opens the file and closes it again automatically
with open(json_file, encoding="utf-8") as f:
    contacts = json.load(f)   # file -> dict (no "s": it reads a file)

for name, info in contacts.items():
    print(name, info["phone"])
