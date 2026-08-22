# Creating a person disctionary representing Sir APJ Abdul Kalam
person = {
    'first_name' : 'Abdul',
    'last_name' : 'Kalam',
    'age' : '83',
    'place' : 'Tamilnadu',
}
name = f"{person['first_name']} {person['last_name']}"
age = person['age']
location = person['place']

print(f"{name} is a scientist and former president of India, He is {age} years old and he is from {location}")

#favourite numbers of my classmates
favourite_numbers = {
    'Rafiq' : 3,
    'Mahesh' : 4,
    'Thaslim' : 8,
    'Kumar' : 10,
}

for name, number in favourite_numbers.items():
    print(f"{name}'s favourite number is {number}")

#Trying to create an actual dictionay which is a glossary
glossary = {
    "Algorithm" : "A step by step set of instructions",
    "Variable" : "A container to store values",
    "Syntax" : "A set of rules to code",
    "Compiler" : "A tramslator that translators human readble files for machines",
} 

for word, meaning in glossary.items():
    print(f"\nWord: {word}")
    print(f"Meaning: {meaning}")
