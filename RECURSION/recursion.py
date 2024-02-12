def multiply_by_sum(a: int, b: int) -> int: 
    """Naive implementation."""
    if b == 0:
        return 0
    
    result = a + multiply_by_sum(a, b-1)

    return result


def binary_search(array: list, item):
    """Given a sorted array. Recusive binary search."""
    left, right = 0, len(array) - 1
    mid = (right + left) // 2

    print(f"looking for {item} in {array}")

    if array[mid] == item:
        return True
    
    elif array[mid] < item:
        return binary_search(array[mid+1:], item)
    
    else:
        return binary_search(array[:mid], item)




if __name__ == "__main__":
    print(multiply_by_sum(4, 5))

    print(binary_search([1, 2, 3, 4, 5], 5))