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

my_new_car = Car('ferrari', 'laferrari', 2016)
print(my_new_car.get_descriptive_name())

#Modifying attribute values directly
my_new_car.odometer_reading = 341
my_new_car.read_odometer()

#Modifying attribute values through a method
my_new_car.update_odometer(348)
my_new_car.read_odometer()