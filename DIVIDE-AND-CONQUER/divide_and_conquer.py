from functools import partial

import numpy as np

printf = partial(print, end="\n\n", sep="\t")


def find_max(array: list):
    return _find_max(0, len(array) - 1, array)


def _find_max(i: int, j: int, array: list):

    if i == j:
        return array[i]

    mid = (i + j) // 2

    return max(_find_max(i, mid, array), _find_max(mid + 1, j, array))


def mergesort(array: list):
    if len(array) > 1:
        mid = len(array) // 2
        left = mergesort(array[:mid])
        right = mergesort(array[mid:])
        array = _merge(left, right)
    return array


def _merge(left_array: list, right_array: list):
    result = []
    i, j = 0, 0

    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            result.append(left_array[i])
            i += 1
        else:
            result.append(right_array[j])
            j += 1

    while i < len(left_array):
        result.append(left_array[i])
        i += 1

    while j < len(right_array):
        result.append(right_array[j])
        j += 1

    return result


def quicksort(array: list) -> list:
    """Last element is pivot implementation."""
    _quicksort(array, 0, len(array) - 1)
    return array


def _quicksort(array: list, start: int, end: int):
    """Recursive quicksort."""
    if end <= start:
        return

    p = _pivot(end, array, start - 1, start)

    _quicksort(array, start, p - 1)
    _quicksort(array, p + 1, end)


def _pivot(p: int, array: int, i: int, j: int) -> int:
    """
    Recursively sort the array in place around pivot.
    Returns pivot's new index.
    """
    if j == p:
        array[i + 1], array[p] = array[p], array[i + 1]
        return i + 1

    if array[j] < array[p]:
        i += 1
        array[i], array[j] = array[j], array[i]

    return _pivot(p, array, i, j + 1)


if __name__ == "__main__":
    array = np.random.randint(0, 500, (100,))

    printf("Div&Con max: ", find_max(array))
    printf("Numpy max: ", array.max())

    A = list(np.random.randint(0, 20, (5,)))
    printf("Random: ", A)
    printf("Merge Sort: ", mergesort(A))
    printf("Quick Sort: ", quicksort(A))

    B = [10, 15, 6, 15, 12]
    printf("Example: ", B)
    printf("Quick Sort: ", quicksort(B))

    C = [9, 9, 12, 9, 9]
    printf("Example: ", C)
    printf("Quick Sort: ", quicksort(C))
