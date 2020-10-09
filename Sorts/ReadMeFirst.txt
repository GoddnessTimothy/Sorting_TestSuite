How to add a new sort to the test suite

1. Update settings.ini and add 3 new entries:
    a. SORT_TYPE_TEST_CASES
    b. SORT_TYPE_RESULTS
    c. EXPECTED_SORT_TYPE_RESULTS
2. Update 'settings.py' to read in the new entries added to settings.ini
3. In 'Sort_Test_Cases.py', add an 'elif' to include your new sort and to call the new sort function.
4. In 'main.py', update 'sort_type' and verify your results the same way I did for selection and insertion sort.
5. Navigate to the sort_type/Test_Cases directory and run 'diff EXPECTED_SORT_TYPE_RESULTS SORT_TYPE_RESULTS'. If you
    do not get an output, both files match.