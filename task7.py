# Task 7: Arithmetic Progression

def arithmetic_progression(max_value):
    terms = [3 * i for i in range(1, (max_value // 3) + 1)]
    return terms, sum(terms), sum(x ** 2 for x in terms)

# Get user input
max_value_ap = int(input("Enter the maximum value for the arithmetic progression: "))
ap_terms, ap_sum, ap_sum_squared = arithmetic_progression(max_value_ap)

# Print results
print("Arithmetic Progression Terms:", ap_terms)
print("Sum of Terms:", ap_sum)
print("Sum of Squared Terms:", ap_sum_squared)
