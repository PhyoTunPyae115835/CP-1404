"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")

# 1. A ValueError will occur if the user inputs something that cannot be converted to an integer.
# 2. A ZeroDivisionError will occur if the user enters 0 as the denominator.
# 3. The code can be changed to prevent a ZeroDivisionError by checking whether the denominator is zero before performing the division.