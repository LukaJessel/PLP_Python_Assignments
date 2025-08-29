from abc import ABC, abstractmethod

# Base class using ABC for enforcing move() implementation
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

# Derived classes
class Car(Vehicle):
    def move(self):
        print("Driving on the road. 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky. ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water. 🚢")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling along the path. 🚲")

# List of vehicles
vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Polymorphic call
for vehicle in vehicles:
    vehicle.move()
