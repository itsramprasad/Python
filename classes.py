Write a Python program that defines a Car class with attributes like make, model, and year, and methods like start() to start the car and stop() to stop it.

# Code:

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_started = False  # to keep track of the car's state

    def start(self):
        if not self.is_started:
            print(f"The {self.year} {self.make} {self.model} is starting.")
            self.is_started = True
        else:
            print(f"The {self.year} {self.make} {self.model} is already running.")

    def stop(self):
        if self.is_started:
            print(f"The {self.year} {self.make} {self.model} is stopping.")
            self.is_started = False
        else:
            print(f"The {self.year} {self.make} {self.model} is already stopped.")

# Demonstrating the Car class
print("---------Car Class Demonstration-----------")
my_car = Car("Hyundai", "i20 asta", 2020)   
print(f"My Car: {my_car.make} {my_car.model} ({my_car.year})")

my_car.start()
my_car.start()   # trying to start again
my_car.stop()
my_car.stop()    # trying to stop again


# Output:	---------Car Class Demonstration-----------
#        My Car: Hyundai I20 asta  (2020)
# The 2020 Hyundai I20 asta  is starting.
#	The 2020 Hyundai I20 asta  is already running.
#	The 2020 Hyundai I20 asta  is stopping.

#	The 2020 Hyundai I20 asta  is already stopped.
