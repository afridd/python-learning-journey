# Working with classes and instances
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a netly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's milage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value
        Reject the change ifit attempts to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

my_new_car = Car('ferrari', 'laferrari', 2016)
print(my_new_car.get_descriptive_name())

#Modifying attribute values directly
my_new_car.odometer_reading = 341
my_new_car.read_odometer()

#Modifying attribute values through a method
my_new_car.update_odometer(348)
my_new_car.read_odometer()

#Incrementing an attributes value  through a method
my_used_car = Car('Mazda', 'rx7', 2008)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

#Inheritance
#The __init__() method for a child class

class Battery:
    """A simple attemp to model a battery for an electric car"""

    def __init__(self, battery_size=102):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        elif self.battery_size == 102:
            range = 530

        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Represemt aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()

my_royce = ElectricCar('rollsroyce', 'spectre', 2026)
print(my_royce.get_descriptive_name())
my_royce.battery.describe_battery()
my_royce.battery.get_range()

#Icecream stand class that stores a list of icecream flavours
class Icecreamshop:
    """Represent an icecream shop"""

    def __init__(self, shop_name, flavours):
        self.shop_name = shop_name
        self.flavours = flavours

    def describe_shop(self):
        """Display the shop name and available flavours"""
        print(f"{self.shop_name} serves delicious {self.flavours} icecream")
    
    def open_shop(self):
        """Display a message indicating the shop is open."""
        print(f"{self.shop_name} is now open.")

shop = Icecreamshop("Badkin Robin", "Chocolate")

shop.describe_shop()
shop.open_shop()