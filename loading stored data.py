from pathlib import Path
import json

path = Path("python-learning-journey/numbers.json")
contents =path.read_text()
numbers = json.loads(contents)

print(numbers)
