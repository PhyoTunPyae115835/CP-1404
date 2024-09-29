"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

BONUS = 1000

sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < BONUS:
        total_sales = sales + (sales * 0.1)
    else:
        total_sales = sales + (sales * 0.15)

    print(f"Final amount with bonus is: ${total_sales:.2f}")

    sales = float(input("Enter sales: $"))

print("Exiting the program.")  #loop break
