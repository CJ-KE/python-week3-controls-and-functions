# Defining the function to calculate the discounted price
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompting the user to enter the original price and discount percentage
try:
    original_price = float(input("Enter the original price: "))
    discount = float(input("Enter the discount percentage: "))

    # Call the function and get the final price
    final_price = calculate_discount(original_price, discount)

    # Print the appropriate result
    if discount >= 20:
        print(f"Discount applied. Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price: ${original_price:.2f}")
except ValueError:
    print("Please enter valid numeric values.")
