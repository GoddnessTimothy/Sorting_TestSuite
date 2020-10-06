from Sorts.selection_sort.selection_sort import selection_sort
from Sorts.insertion_sort.insertion_sort import insertion_sort
import filecmp


def sort_test_cases(in_data, out_data, expected_data, sort_type=""):
    sorted_list = []
    print(f"Sorting using {sort_type} SORT...")
    with open(in_data, "r") as input_data, open(out_data, "w") as output_data, open(expected_data, "w") as exp_data:
        for line in input_data:
            # Each line is read in as a list of strings. Convert each item in list to an int before sorting.
            unsorted_list = list(map(lambda x: int(x), line.split(",")))
            # Sort each list in 'SELECTION_SORT_TESTCASES' line by line.
            if sort_type == "selection".upper():
                sorted_list = selection_sort(unsorted_list)
            elif sort_type == "insertion".upper():
                sorted_list = insertion_sort(unsorted_list)
            # Sort using sorted() by default.
            else:
                sorted_list = sorted(unsorted_list)
            # Write sorted list to "SELECTION_SORT_RESULTS".
            output_data.write(str(sorted_list).replace("[","").replace("]","") + '\n')
            # Write sorted list (sorted with built-in sorted function) to "EXPECTED_RESULTS".
            exp_data.write(str(sorted(list(unsorted_list))).replace("[","").replace("]","") + "\n")


def verify_sort(results, expected_results):
    # If true, both files match (content-wise)
    return filecmp.cmp(results, expected_results, shallow=False)
