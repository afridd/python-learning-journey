from pathlib import Path
import json #Use json to store(dump) and retrieve(load) data

numbers = [2, 3, 5, 7, 11, 13]
path = Path("python-learning-journey/numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)

username = input("What is your name? ")
location = Path("python-learning-journey/usernames.json")
values = json.dumps(username)
location.write_text(values)

print(f"We'll remember youu when you come back, {username}!")