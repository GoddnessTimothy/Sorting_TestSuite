def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        current_value = A[i]
        position = i
        while position > 0 and A[position - 1] > current_value:
            A[position] = A[position - 1]
            position = position - 1
        A[position] = current_value
    return A