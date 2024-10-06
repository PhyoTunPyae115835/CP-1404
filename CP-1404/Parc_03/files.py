# # Asking the user for their name and writing it to name.txt
# name = input("What is your name? ")
#
# out_file = open('name.txt', 'w')
# out_file.write(name)
#
# out_file.close()

# # Open the file for reading
# in_file = open('name.txt', 'r')
# name = in_file.read().strip()
# in_file.close()
#
# print(f"Hi {name}!")

# # Open numbers.txt and read only the first two numbers
# with open('numbers.txt', 'r') as in_file:
#     first_number = int(in_file.readline())
#     second_number = int(in_file.readline())
#
# sum_of_two = first_number + second_number
# print(f"The sum of the first two numbers is: {sum_of_two}")

# Open numbers.txt and read all the numbers
with open('numbers.txt', 'r') as in_file:
    total = 0
    for line in in_file:
        total += int(line)

print(f"The total sum of all numbers is: {total}")







