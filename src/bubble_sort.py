def bubble_sort(arr):
    """Use the bubble sort algorithm to sort a list of integers.

    Args:
        arr (list of int): The list of unsorted integers.

    Returns:
        list of int: The sorted list of integers.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
