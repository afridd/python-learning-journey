#importing functions as modulles
from cat import Cat
from functions import make_pizza

my_cat = Cat("Tom", 3)

my_cat.sit()
my_cat.roll_over()

make_pizza(22, 'chicken')
make_pizza(8, 'mutton', 'olives', 'onions')

