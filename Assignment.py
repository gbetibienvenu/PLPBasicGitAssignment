def calculate_discount(price, discount_percent):
    # It  check if the discount is 20% or higher
    if discount_percent >= 20:
        # While this calculate the final price after applying the discount
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # This return the original price if discount is less than 20%
        return price

# This function is to get valid input from the user
def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

# It prompt the user for the original price and discount percentage
original_price = get_valid_input("Enter the original price of the item: ")
discount_percentage = get_valid_input("Enter the discount percentage: ")

# This calculate the final price by  using the calculate_discount function
final_price = calculate_discount(original_price, discount_percentage)

# It print the final price
if final_price < original_price:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The original price is: ${original_price:.2f}")
