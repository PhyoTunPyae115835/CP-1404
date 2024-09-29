# # a: Count in 10s from 0 to 100
# for i in range(0, 101, 10):
#     print(i, end=' ')
# print()

# # b: Count down from 20 to 1
# for i in range(20, 0, -1):
#     print(i, end=' ')
# print()

# # c: Ask the user for a number and print that many stars on one line
# n = int(input("Enter number of stars: "))
# print('*' * n)

# d: Ask the user for a number and print increasing lines of stars
n = int(input("Enter number of lines: "))
for i in range(1, n + 1):
    print('*' * i)

