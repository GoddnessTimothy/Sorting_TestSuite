from Sorts.Sort_Test_Cases import sort_test_cases, verify_sort
from Sorts.Generate_Random_Lists import generate_random_lists

INSERTION_SORT_TESTCASES = r"/Users/tim/PycharmProjects/DSA/Sorts/Test_Cases/SORT_TESTCASES"
INSERTION_SORT_RESULTS = r"/Users/tim/PycharmProjects/DSA/Sorts/insertion/Test_Cases/INSERTION_SORT_RESULTS"
EXPECTED_INSERTION_SORT_RESULTS = r"/Users/tim/PycharmProjects/DSA/Sorts/insertion/Test_Cases" \
                                  r"/EXPECTED_INSERTION_SORT_RESULTS "

SELECTION_SORT_TESTCASES = r"/Users/tim/PycharmProjects/DSA/Sorts/Test_Cases/SORT_TESTCASES"
SELECTION_SORT_RESULTS = r"/Users/tim/PycharmProjects/DSA/Sorts/selection/Test_Cases/SELECTION_SORT_RESULTS"
EXPECTED_SELECTION_SORT_RESULTS = r"/Users/tim/PycharmProjects/DSA/Sorts/selection/Test_Cases" \
                                  r"/EXPECTED_SELECTION_SORT_RESULTS "

if __name__ == "__main__":

    generate_random_lists()

    sort_test_cases(SELECTION_SORT_TESTCASES,
                    SELECTION_SORT_RESULTS, EXPECTED_SELECTION_SORT_RESULTS, "selection")
    if verify_sort(SELECTION_SORT_RESULTS, EXPECTED_SELECTION_SORT_RESULTS):
        print("Selection Sort: Your sort results matches the expected results.")
    else:
        print("Selection Sort: Something isn't right. Some or all of your results do not match.")

    sort_test_cases(INSERTION_SORT_TESTCASES, INSERTION_SORT_RESULTS, EXPECTED_INSERTION_SORT_RESULTS, "insertion")
    if verify_sort(INSERTION_SORT_RESULTS, EXPECTED_INSERTION_SORT_RESULTS):
        print("Insertion Sort: Your sort results matches the expected results.")
    else:
        print("Insertion Sort: Something isn't right. Some or all of your results do not match.")
