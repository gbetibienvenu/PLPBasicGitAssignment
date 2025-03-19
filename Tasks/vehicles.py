# Define Vehicle, Car, Plane, and Boat classes here
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving my own car 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying up with my jet ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing stuff here 🚤"

