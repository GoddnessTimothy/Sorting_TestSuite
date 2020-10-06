"""
Algorithm for Selection Sort
1) Start from index i (initially 0) until index len(A)-1
   1a) Find the mimimum item in remainder of the list
2) Swap the two items.
3) Repeat until index reaches index len(A)-1.
"""


def selection_sort(A):
    # Get the length of A.
    n = len(A)
    for i in range(n - 1):
        # Find the mimimum of the remainder of the list and swap with current index.
        for j in range(i + 1, n):
            if (A[j] < A[i]):
                # Swap A[j] with A[i].
                tmp = A[j]
                A[j] = A[i]
                A[i] = tmp
    return A
