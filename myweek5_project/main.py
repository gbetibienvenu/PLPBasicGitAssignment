#Files has been  Importing here 
from smartphone import Smartphone, Smartwatch
from vehicles import Vehicle, Car, Plane, Boat

# Example usage for Smartphone and Smartwatch
phone = Smartphone("Apple", "iPhone 14", "256GB", 999)
watch = Smartwatch("Samsung", "Galaxy Watch 5", "48 hours", 299)

print(phone.call("+2349136710349"))  # Call from Apple iPhone 14.
print(watch.browse("https://academy.powerlearnprojectafrica.org"))  # Browsing academy.powerlearnprojectafrica.org

# This are the  Examples of the  usage for Vehicles
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())

