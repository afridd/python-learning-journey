from pathlib import Path
import json #Use json to store(dump) and retrieve(load) datas

numbers = [2, 3, 5, 7, 11, 13]
path = Path("python-learning-journey/numbers.json")
contents = json.dumps(numbers)
path.write_text(contents)

def get_stored_username(location):
    """Get stored username if available"""
    if location.exists():
            values = location.read_text()
            username = json.loads(values)
            return username
    else:
         return None

def get_new_username(location):
    """Prompt for new username"""
    username = input("What is your name? ")
    values = json.dumps(username)
    location.write_text(values)
    return username

    
def greet_user():
    """Greet the user by name."""
    location = Path("python-learning-journey/usernames.json")
    username = get_stored_username(location)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(location)
        print(f"We'll remember youu when you come back, {username}!")


greet_user()
