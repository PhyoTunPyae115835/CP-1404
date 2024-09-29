
number_of_item = int(input("Number of items: "))
while number_of_item < 0:
    print("Invalid number of items!")
    number_of_item = int(input("Number of items: "))

total_price = 0

for i in range(1, number_of_item + 1):
    price = float(input(f"Price of item {i}: "))
    total_price += price

if total_price > 100:
    total_price *= 0.9

print(f"Total price for {number_of_item} items is ${total_price:.2f}")