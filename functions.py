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

#Using a function with a while loop
def fullname(firstname, lastname):
    """Trying to get input from  user using while loop"""
    name = f"{firstname} {lastname}"
    return name.title()

#giving option to quit the loop
while True:
    print("\nPlease tell me your name...")
    print("\nEnter q at anytime to stop")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = fullname(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

#Function that retuns country and capital
def capital_country(capital, country): 
    """Return place fully formatted"""
    place = f"{capital}, {country}"
    return place
while True:
    print("Give the name of the capital and country")
    print("Enter 'q' to stop")

    cap = input("Capital: ")
    if cap == 'q':
        break
    nat = input("Country: ")
    if nat == 'q':
        break

    place_name = capital_country(cap, nat)
    print(f"\n{place_name}")

#Making a dictionary in a function
def build_person(first_name, last_name,age=None):
    """Return a dicttionary of information about a person."""
    person = {'first' : first_name, 'last' : last_name}
    if age:
        person['age'] = age
    return person
music_director =build_person('harris', 'jayaraj', age=51)
print(music_director)

#passing a list
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = {'vijay', 'ajith', 'surya', 'karthi'}
greet_users(usernames)

#Modifying a list in a function
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left
    Move each design to completed_models after printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'car toy']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#Message semt list and function
def send_msg(send, sent):
    """Stimulate printing messages to be sent"""
    while send:
        storage = send.pop(0)
        print(f"Sending {storage}...")
        sent.append(storage)
def sent_msg(sent):
    """Show all the messages that were sent"""
    for msg in sent:
        print(f"Sent {msg}")
messages = ['HI', 'How are you', 'Bye']
sent_messages = []
send_msg(messages,sent_messages)
sent_msg(sent_messages)

#Passing arbitrary number of arguments
def make_pizza(size,*toppings):
    """Summarize the pizza that we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16, 'paneer', 'extra cheese')
make_pizza(8, 'mushroom', 'capsicum', 'olive')

#Using arbritary keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Jon', 'Snow', 
                             location='Winterfell', 
                             field='King in the North',
                             lover='Daenerys',
                             identity='Real King of the Seven Kingdoms',
                             real_name='Aegon Targaryen')

print(user_profile)
