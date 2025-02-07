# Task 9: Random Number Function

import random

def get_random_number():
    return random.randint(1, 6)

# Print out the number where the function is called
random_number = get_random_number()
print("Random Number:", random_number)
