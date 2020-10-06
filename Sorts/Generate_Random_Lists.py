import random


# Generate a list of random numbers
def generate_random_lists(test_cases_out):
    test_cases = open(test_cases_out, "w")
    for i in range(10):
        random_list = random.sample(range(0, 15), 5)
        # Convert list to a string and write to file.
        test_cases.write(
            str(random_list).replace("[", "").replace("]", "") + "\n")
