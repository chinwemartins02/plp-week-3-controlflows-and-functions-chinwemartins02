def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying the discount.
    If the discount is 20% or higher, apply it; otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount = price * discount_percent // 100  # Integer division for discount
        final_price = price - discount
        return final_price
    else:
        return price

# Prompt the user for inputs
original_price = int(input("Enter the original price of the item (integer): "))
discount_percentage = int(input("Enter the discount percentage (integer): "))

# Calculate the final price using the function
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if final_price == original_price:
    print(f"No discount applied. The original price is: {original_price}")
else:
    print(f"Discount applied. The final price is: {final_price}")
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying the discount.
    If the discount is 20% or higher, apply it; otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount = price * discount_percent // 100  # Integer division for discount
        final_price = price - discount
        return final_price
    else:
        return price

# Prompt the user for inputs
original_price = int(input("Enter the original price of the item (integer): "))
discount_percentage = int(input("Enter the discount percentage (integer): "))

# Calculate the final price using the function
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if final_price == original_price:
    print(f"No discount applied. The original price is: {original_price}")
else:
    print(f"Discount applied. The final price is: {final_price}")
