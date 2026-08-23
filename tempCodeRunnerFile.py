def describe_pet(animal_type, pet_name):
    """Diplaying information about pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")

describe_pet('parrot','zazu')
describe_pet('cat','dairy milk')