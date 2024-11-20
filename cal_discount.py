def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the final price after applying the discount
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        # Return the original price if no discount is applied
        return price

# Prompt the user for the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function and print the result
final_price = calculate_discount(price, discount_percent)

# Print the final price or the original price if no discount was applied
print(f"The final price is: {final_price}")
