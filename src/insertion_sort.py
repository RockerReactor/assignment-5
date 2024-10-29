def insertion_sort(arr):
    """Use the insertion sort algorithm to sort a list of integers.

    Args:
        arr (list of int): The list of unsorted integers.

    Returns:
        list of int: The sorted list of integers.
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # moves elements that are greater than key up a position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
