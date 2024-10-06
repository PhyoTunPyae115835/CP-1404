import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# 1. Smallest possible value: 5, Largest possible value: 20
# 2. Smallest possible value: 3, Largest possible value: 9. Line 2 chouldn't have produced a 4,  because the step is 2, and starting at 3 will only allow odd numbers (3, 5, 7, 9).
# 3. Smallest possible value: 2.5, Largest possible value: 5.5


# Code to produce a random number between 1 and 100 inclusive.
import random

random_number = random.randint(1, 100)
print(random_number)
