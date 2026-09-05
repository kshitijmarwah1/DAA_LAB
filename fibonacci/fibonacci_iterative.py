"""
DAA Lab - Fibonacci Program 2: Iterative Approach
Time Complexity: O(n)   Space Complexity: O(1)
"""
import time
import tracemalloc


def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    n = int(input("Enter n: "))

    tracemalloc.start()
    start = time.perf_counter()

    result = fib_iterative(n)

    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("Fibonacci(", n, ") =", result)
    print("Time Taken =", end - start, "seconds")
    print("Current Memory =", current, "bytes")
    print("Peak Memory =", peak, "bytes")
