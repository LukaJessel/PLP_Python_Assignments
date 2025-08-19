def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        discount = price * (discount_percentage / 100)
        final_price = price - discount
        return final_price
    else:
        return price
    
# prompt for user input
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# calculate final price
final_price = calculate_discount(original_price, discount)

# print results
if discount >= 20:
    print(f"The final price after a {discount}% discount is: ${final_price:.2f}")
else:
    print(f"No discount applied. The price remains: ${final_price:.2f}")