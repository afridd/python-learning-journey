#Defining a function
def greet_user(username):
    """Displaying a simple message"""
    print(f"Hello, {username.title()}!")

greet_user("rose")

#Positional arguments
def describe_pet(animal_type, pet_name):
    """Diplaying information about pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")

describe_pet('parrot','zazu')
describe_pet('cat','dairy milk')

#Keyword arguments
describe_pet(pet_name='Jerry',animal_type='Mouse')

#default arguments
def describe_pet(animal_type, pet_name='Tom'):
    """Diplaying information about pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")
    
describe_pet('cat')