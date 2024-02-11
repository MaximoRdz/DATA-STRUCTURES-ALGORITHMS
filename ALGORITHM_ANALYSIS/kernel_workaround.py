import time

import csv
import numpy as np


def runtime(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        dt = time.time() - t1
        return dt
    return wrapper


@runtime
def sum_for_loop(N: int):
    result = 0
    for i in range(1, N+1):
        result += i
    return result


@runtime
def sum_built_in(N: int):
    return sum(range(1, N+1))


@runtime
def sum_recursive(N: int):

    if N == 0:
        return 0
    
    result = N + sum_recursive(N-1)

    return result


# cache = {}
# @runtime
# def sum_memoization(N: int):
#     if N == 0:
#         return 0
    
#     if N in cache:
#         return cache[N]
    
#     result = N + sum_memoization(N-1)

#     cache[N] = result

#     return result


@runtime
def sum_gauss(N: int):
    return 0.5 * N * (N + 1)


test_functions = {
    "For Loop": np.vectorize(sum_for_loop),
    "Built-in": np.vectorize(sum_built_in),
    # "Recursion": np.vectorize(sum_recursive),
    # "Memoization": np.vvectorize(sum_memoization),
    "Gauss": np.vectorize(sum_gauss)
    }


def save(data, header):
    with open("./ALGORITHM_ANALYSIS/data.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        writer.writerow(data)


def main():
    exp_max = 5

    N = np.array([pow(10, i) for i in range(1, exp_max+1)])

    function_times = {}

    for key, func in test_functions.items():

        function_times[key] = func(N)

        print(f"Execution of '{key}' finished.")

        # cache.clear()   # clear cache of memoization function

    save(function_times, function_times.keys())

if __name__ == "__main__":
    main()