class Car:
    def move(self):
        return "Driving 🚗"

class Plane:
    def move(self):
        return "Flying ✈️"

class Bicycle:
    def move(self):
        return "Cycling 🚲"

# List of vehicles
vehicles = [Car(), Plane(), Bicycle()]

# Demonstrate polymorphism
for vehicle in vehicles:
    print(vehicle.move())
