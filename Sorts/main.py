from Sorts.Sort_Test_Cases import sort_test_cases, verify_sort
from Sorts.Generate_Random_Lists import generate_random_lists
import configparser

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.sections()
    config.read('/Users/tim/PycharmProjects/DSA/Sorts/settings.ini')

    INSERTION_SORT_TESTCASES = config['INSERTION SORT TESTCASES']['INSERTION_SORT_TESTCASES']
    INSERTION_SORT_RESULTS = config['INSERTION SORT TESTCASES']['INSERTION_SORT_RESULTS']
    EXPECTED_INSERTION_SORT_RESULTS = config['INSERTION SORT TESTCASES']['EXPECTED_INSERTION_SORT_RESULTS']

    SELECTION_SORT_TESTCASES = config['SELECTION SORT TESTCASES']['SELECTION_SORT_TESTCASES']
    SELECTION_SORT_RESULTS = config['SELECTION SORT TESTCASES']['SELECTION_SORT_RESULTS']
    EXPECTED_SELECTION_SORT_RESULTS = config['SELECTION SORT TESTCASES']['EXPECTED_SELECTION_SORT_RESULTS']

    generate_random_lists(SELECTION_SORT_TESTCASES)
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
