def quick_sort(arr):
    """Use the quick sort algorithm to sort a list of integers.

    Args:
        arr (list of int): The list of unsorted integers.

    Returns:
        list of int: The sorted list of integers.
    """
    n = len(arr)
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        # makes an array of values less than or equal to pivot
        less_than = [x for x in arr[1:] if x <= pivot]
        # makes an array of values greater than pivot
        greater_than = [x for x in arr[1:] if x > pivot]

        # recursive quicksort
        return quick_sort(less_than) + [pivot] + quick_sort(greater_than)
