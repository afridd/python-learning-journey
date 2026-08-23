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

#Returning values from functions
def fullname(firstname, lastname, middlename=''):
    """Return a full name, neatly formatted"""
    if middlename:
        name = f"{firstname} {middlename} {lastname}"
    else:
        name = f"{firstname} {lastname}"
    return name.title()

user1 = fullname('jon', 'snow')
print(user1)
user2 = fullname('daenerys', 'targaryen', 'stormborn')
print(user2)
