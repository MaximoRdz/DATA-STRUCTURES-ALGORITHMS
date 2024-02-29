import numpy as np


def find_max(array: list):
    return _find_max(0, len(array) - 1, array)


def _find_max(i: int, j: int, array: list):

    if i == j:
        return array[i]
    
    mid = (i + j) // 2

    return max(_find_max(i, mid, array), _find_max(mid + 1, j, array))


def mergesort(array: list):
    return _mergesort(0, len(array) - 1, array)


def _mergesort(i: int, j: int, array: list):
    mid = (i + j) // 2

    return _merge(_mergesort(i, mid, array), _mergesort(mid + 1, j, array))


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

    while j < len(right_array):
        result.append(right_array[j])
    
    return result


if __name__ == "__main__":
    array = np.random.randint(0, 500, (100,))

    print("Divide n conquer max: ", find_max(array))
    print("Numpy max: ", array.max())

    A = list(np.random.randint(0, 20, (5,)))
    print(A)
    print("Sorted: ", mergesort(A))

