from Sorts.Sort_Test_Cases import sort_test_cases, verify_sort
from Sorts.Generate_Random_Lists import generate_random_lists
from Sorts.Settings import *

if __name__ == "__main__":
    generate_random_lists(SORT_TEST_CASES)
    sort_type = "SELECTION"
    sort_test_cases(SELECTION_SORT_TESTCASES,
                    SELECTION_SORT_RESULTS, EXPECTED_SELECTION_SORT_RESULTS, sort_type)
    if verify_sort(SELECTION_SORT_RESULTS, EXPECTED_SELECTION_SORT_RESULTS):
        print(f"{sort_type}: Your sort results matches the expected results.")
    else:
        print(f"{sort_type}: Something isn't right. Some or all of your results do not match.")

    sort_type = "INSERTION"
    sort_test_cases(INSERTION_SORT_TESTCASES, INSERTION_SORT_RESULTS, EXPECTED_INSERTION_SORT_RESULTS,sort_type)
    if verify_sort(INSERTION_SORT_RESULTS, EXPECTED_INSERTION_SORT_RESULTS):
        print(f"{sort_type}:Your sort results matches the expected results.")
    else:
        print(f"{sort_type}: Something isn't right. Some or all of your results do not match.")
