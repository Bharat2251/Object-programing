# Define the factorials function
def factorials(n: int) -> dict:
    factorial_dict = {}
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        factorial_dict[i] = factorial
    return factorial_dict

# Test the function with a different number
k = factorials(7)
print(k[1]) 
print(k[3])  
print(k[7])
