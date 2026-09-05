"""
DAA Lab - Fibonacci Program 3: Memoized (Dynamic Programming / Top-Down) Approach
Time Complexity: O(n)   Space Complexity: O(n)
"""
import time
import tracemalloc


def fib_memoized(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_memoized(n - 1, memo) + fib_memoized(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    n = int(input("Enter n: "))

    tracemalloc.start()
    start = time.perf_counter()

    result = fib_memoized(n)

    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("Fibonacci(", n, ") =", result)
    print("Time Taken =", end - start, "seconds")
    print("Current Memory =", current, "bytes")
    print("Peak Memory =", peak, "bytes")
