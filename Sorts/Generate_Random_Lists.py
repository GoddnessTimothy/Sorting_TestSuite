import random


# Generate a list of random numbers
def generate_random_lists(test_cases_out):
    test_cases = open(test_cases_out, "w")
    for i in range(10):
        # Generate 20 random ints between 0 and 100000
        randomList = random.sample(range(0, 15), 5)
        # Convert list to a string and write to file.
        test_cases.write(
            str(randomList).replace("[", "").replace("]", "") + "\n")


