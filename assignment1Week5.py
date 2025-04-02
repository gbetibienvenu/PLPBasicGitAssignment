class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Smartphone Brand: {self.brand}, Model: {self.model}"

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Book Title: {self.title}, Author: {self.author}"

class Superhero:
    def __init__(self, name, superpower):
        self.name = name
        self.superpower = superpower

    def display_info(self):
        return f"Superhero: {self.name}, Superpower: {self.superpower}"

# Test classes
smartphone = Smartphone("Apple", "iPhone 14")
book = Book("1984", "George Orwell")
superhero = Superhero("Spider-Man", "Web-Slinging")

print(smartphone.display_info())
print(book.display_info())
print(superhero.display_info())
