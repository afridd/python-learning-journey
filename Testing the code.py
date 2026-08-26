#importing functions as modulles
from cat import Cat
from functions import make_pizza
from classes import ElectricCar

my_cat = Cat("Tom", 3)

my_cat.sit()
my_cat.roll_over()

make_pizza(22, 'chicken')
make_pizza(8, 'mutton', 'olives', 'onions')

my_royce = ElectricCar('rollsroyce', 'spectre', 2026)
print(my_royce.get_descriptive_name())
my_royce.battery.describe_battery()
my_royce.battery.get_range()