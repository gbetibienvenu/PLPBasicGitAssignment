# Define Smartphone and Smartwatch classes here
class Smartphone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def call(self, number):
        return f"Calling {number} from {self.brand} {self.model}."

    def browse(self, website):
        return f"Browsing {website} on {self.brand} {self.model}."

class Smartwatch(Smartphone):
    def __init__(self, brand, model, battery_life, price):
        super().__init__(brand, model, "None", price)
        self.battery_life = battery_life

    def track_steps(self, steps):
        return f"{self.brand} {self.model} tracked {steps} steps today!"

    def browse(self, website):
        return f"Browsing {website} is limited on {self.brand} {self.model} due to its smaller screen."

