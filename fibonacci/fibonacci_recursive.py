"""
DAA Lab - Fibonacci Program 1: Naive Recursive Approach
Time Complexity: O(2^n)   Space Complexity: O(n) (recursion stack)
"""
import time
import tracemalloc


def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


if __name__ == "__main__":
    n = int(input("Enter n: "))

    tracemalloc.start()
    start = time.perf_counter()

    result = fib_recursive(n)

    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("Fibonacci(", n, ") =", result)
    print("Time Taken =", end - start, "seconds")
    print("Current Memory =", current, "bytes")
    print("Peak Memory =", peak, "bytes")
