"""
[1,4,5,23,19,45,20,17]

[1,4,5,23] [17,19,20,45]

[1,4] [5,23] [19,45] [17,20]

[1] [4] [5] [23] [19] [45] [20] [17]
"""


def merge(r, l, A):
    length_A = len(A)
    length_l = len(l)
    length_r = len(r)
    i = 0
    j = 0
    k = 0

    while i < length_l and j < length_r:
        """ 
        Compare the item in the left halve to the item in the right halve. If item in left halve is smaller,
        write it to list A.
        """
        if l[i] <= r[j]:
            A[k] = l[i]
            i = i + 1
        else:
            """
            The item in the right half is smaller so write the item to list A.
            """
            A[k] = r[j]
            j = j + 1
        k = k + 1
    # If there are remaining items in the left list, insert them into list A.
    while i < length_l:
        A[k] = l[i]
        k = k + 1
        i = i + 1
    # If there are remaining items in the right list, insert them into list A.
    while j < length_r:
        A[k] = r[j]
        k = k + 1
        j = j + 1


def merge_sort(A):
    n = len(A)
    if n < 2:
        return
    mid = n // 2
    left = A[:mid]
    right = A[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, A)
    return A