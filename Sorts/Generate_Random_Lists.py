import random

# Generate a list of random numbers
def generate_random_lists():
    SELECTION_SORT_TESTCASES = open(
        r"/Users/tim/PycharmProjects/DSA/Sorts/Test_Cases/SORT_TESTCASES", "w")
    for i in range(10):
        # Generate 20 random ints between 0 and 100000
        randomList = random.sample(range(0, 15), 5)
        # Convert list to a string and write to file.
        SELECTION_SORT_TESTCASES.write(
            str(randomList).replace("[", "").replace("]", "") + "\n")


