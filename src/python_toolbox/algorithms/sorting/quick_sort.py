from typing import Callable, List, TypeVar

T = TypeVar("T")


def quick_sort(
    arr: List[T], key: Callable[[T], Any] = lambda x: x, reverse: bool = False
) -> List[T]:
    """Sort a list using the quicksort algorithm.

    Args:
        arr: The list to sort.
        key: A function that extracts the comparison key from each element.
        reverse: If True, sort in descending order.

    Returns:
        A new sorted list.

    Time Complexity:
        Average: O(n log n)
        Worst: O(n²)
    Space Complexity:
        O(n)
    """
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if key(x) < key(pivot)]
    middle = [x for x in arr if key(x) == key(pivot)]
    right = [x for x in arr if key(x) > key(pivot)]

    result = quick_sort(left, key, reverse) + middle + quick_sort(right, key, reverse)
    return result if not reverse else result[::-1]
