# user_input.py

# Function to get user input with a prompt
def get_input(prompt):
    return input(prompt)

# Asking for user's details using the function
name = get_input("What's your name? ")
age = get_input("How old are you? ")
location = get_input("Where do you live? ")

# Printing a personalized message
print(f"Hello {name}, you are {age} years old and live in {location}.")
