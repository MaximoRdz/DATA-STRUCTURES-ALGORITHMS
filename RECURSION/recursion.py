import time


def runtime(func):

    def wrapper(*args, **kwargs):
        dt = 0
        N = 10
        for _ in range(N):
            t1 = time.time()
            _ = func(*args, **kwargs)
            dt += time.time() - t1

        return dt / N
    
    return wrapper

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


@runtime
def sum_list(array: list):
    """
    Highly inefficient recursive way of summing a list.
    Creating a new array every time the function makes a
    recursive call is not good. spacial complexity ^
    """
   
    if len(array) == 0:
        return 0
    
    result = array[0]

    result += sum_list(array[1:])

    return result


@runtime
def sum_list_pop(array: list):
    """More efficient algorithm."""

    if len(array) == 0:
        return 0
    
    result = 0

    result = array.pop() + sum_list(array)

    return result


@runtime
def sum_list_index(array: list, ind: int):

    if ind == len(array):
        return 0
    
    result = array[ind]
    result += sum_list_index(array, ind+1)

    return result
    

if __name__ == "__main__":
    print("Multiply by sum: ", multiply_by_sum(4, 5))

    print("Binary search: ", binary_search([1, 2, 3, 4, 5], 5))

    print(f"sum list: {sum_list([1, 2, 3, 4, 5]):5f} s")

    print(f"sum list pop: {sum_list_pop([1, 2, 3, 4, 5]):5f} s")

    print(f"sum list ind: {sum_list_index([1, 2, 3, 4, 5], 0):5f} s")

