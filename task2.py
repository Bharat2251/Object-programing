# Task 2: Lists of Numbers and Strings

# Part 1 - User input
number_list = [int(input("Enter a number: ")) for _ in range(10)]
string_list = [input("Enter a string: ") for _ in range(10)]

# Part 2 - Randomly generated numbers
import random
random_numbers = [random.randint(1, 100) for _ in range(10)]

# Print lists
print("Number List:", number_list)
print("String List:", string_list)
print("Random Number List:", random_numbers)

