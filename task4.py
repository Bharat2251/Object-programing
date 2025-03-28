#Counts how many numbers in the input list are negative.
def count_negative_numbers(numbers):
    return sum(1 for num in numbers if num < 0)

#Counts how many numbers are divides by 2 without reminder even number.
def count_even_numbers(numbers):
    return sum(1 for num in numbers if num % 2 == 0)

#Calculates the sum of all positive numbers in the list that are divisible by 3.
def sum_positive_divisible_by_three(numbers):
    return sum(num for num in numbers if num > 0 and num % 3 == 0)

# Initialize an empty list to store the numbers
numbers_input = []

# Continuously prompt the user to enter numbers until 0 is entered
while True:
    try:
        num = int(input("Enter an integer (0 to stop): "))
        if num == 0:
            break
        numbers_input.append(num)
    except ValueError:
        print("Please enter a valid integer.")

# Task 4
print("Number of negative integers:", count_negative_numbers(numbers_input))

# Task 5
print("Number of even integers:", count_even_numbers(numbers_input))

# Task 6
print("Sum of positive integers divisible by three:", sum_positive_divisible_by_three(numbers_input))


