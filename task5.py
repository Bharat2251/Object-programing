def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
    # Calculate average results for each contestant
    person1_average = (person1["result1"] + person1["result2"] + person1["result3"]) / 3
    person2_average = (person2["result1"] + person2["result2"] + person2["result3"]) / 3
    person3_average = (person3["result1"] + person3["result2"] + person3["result3"]) / 3

    # Find the contestant with the smallest average
    if person1_average < person2_average and person1_average < person3_average:
        return person1
    elif person2_average < person1_average and person2_average < person3_average:
        return person2
    else:
        return person3

# Test the function with the provided example
person1 = {"name": "Bharat", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Parth", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Yatin", "result1": 3, "result2": 1, "result3": 1}

print(smallest_average(person1, person2, person3))
