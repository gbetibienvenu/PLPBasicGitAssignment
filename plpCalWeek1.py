# This is task for week 1 on python module 

def calculator():
    try:
        # Get user input for numbers and operation
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        # Perform the calculation based on the operation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation! Please enter one of +, -, *, /.")
            return

        # Print the result
        print(f"{num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the calculator
calculator()
