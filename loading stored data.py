from pathlib import Path
import json

path = Path("python-learning-journey/numbers.json")
contents =path.read_text()
numbers = json.loads(contents)

print(numbers)


location = Path("python-learning-journey/usernames.json")
values = location.read_text()
username = json.loads(values)

print(f"Welcome back, {username}!")
