<body>
  <h1>Sorting TestSuite</h1>

Sorting testsuite is a small Python framework that allows you to test your sorting algorithms <br />

## Adding a new sort to the test suite.  In this case, I am adding merge sort.
Use the settings.ini file to define the test cases path. <br />
 
[SORTING TEST CASES] <br />
SORT_TESTCASES = PATH_TO_SORT_TESTCASES <br />

[INSERTION SORT TESTCASES] <br />
INSERTION_SORT_TESTCASES = SORT_TESTCASES <br />
INSERTION_SORT_RESULTS = PATH_TO_INSERTION_SORT_RESULTS <br />
EXPECTED_INSERTION_SORT_RESULTS = PATH_TO_EXPECTED_INSERTION_SORT_RESULTS <br />

[SELECTION SORT TESTCASES] <br />
SELECTION_SORT_TESTCASES = SORT_TESTCASES <br />
SELECTION_SORT_RESULTS = PATH_TO_SELECTION_SORT_RESULTS <br />
EXPECTED_SELECTION_SORT_RESULTS = PATH_TO_EXPECTED_SELECTION_SORT_RESULTS <br />

<strong>
[MERGE SORT TESTCASES] <br />
MERGE_SORT_TESTCASES = SORT_TESTCASES <br />
MERGE_SORT_RESULTS = PATH_TO_MERGE_SORT_RESULTS <br />
EXPECTED_MERGE_SORT_RESULTS = PATH_TO_EXPECTED_MERGE_SORT_RESULTS<br />
</strong>

## Add entry to settings.py to reflect the new entry in settings.ini.
MERGE_SORT_TESTCASES = config['MERGE SORT TESTCASES']['MERGE_SORT_TESTCASES'] <br />
MERGE_SORT_RESULTS = config['MERGE SORT TESTCASES']['MERGE_SORT_RESULTS'] <br />
EXPECTED_MERGE_SORT_RESULTS = config['MERGE SORT TESTCASES']['EXPECTED_MERGE_SORT_RESULTS'] <br />

## Update Sort_Test_Cases.py so that merge_sort will be used to sort the test cases.
elif sort_type == "merge".upper(): <br />
    sorted_list = merge_sort(unsorted_list)

## Update main.py code to check if your test cases has been properly sorted with merge sort.
sort_type = "MERGE" <br />
sort_test_cases(MERGE_SORT_TESTCASES, MERGE_SORT_RESULTS, EXPECTED_MERGE_SORT_RESULTS, sort_type) <br />
if verify_sort(MERGE_SORT_RESULTS, EXPECTED_MERGE_SORT_RESULTS): <br />
  print(f"{sort_type}:Your sort results matches the expected results.") <br />
else: <br />
  print(f"{sort_type}: Something isn't right. Some or all of your results do not match.")<br />

## Execute the script and confirm the results.
python main.py

Navigate to merge_sort/Test_Cases directory in your termninal and use: <br />
diff EXPECTED_MERGE_SORT_RESULTS MERGE_SORT_RESULTS <br />
If you don't see any output, the two files match. Python uses a special sort called TimSort to sort. The purpose of comparing these two results is to see if your merge sort matches the results of Python's sort results.
</body>

