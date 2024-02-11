def multiply_by_sum(a: int, b: int) -> int: 
    """Naive implementation."""
    if b == 0:
        return 0
    
    result = a + multiply_by_sum(a, b-1)

    return result


def binary_search(item, array: list, start, end):
    """Given a sorted array."""
    pass




if __name__ == "__main__":
    print(multiply_by_sum(4, -5))