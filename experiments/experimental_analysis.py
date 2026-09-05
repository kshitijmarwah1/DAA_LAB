"""
DAA Lab - Question 1: Experimental Analysis
Runs Bubble Sort, Insertion Sort, Merge Sort and Quick Sort on different
input sizes and input conditions (sorted, reverse-sorted, random) and
records execution time, peak memory usage, and comparison counts.
"""
import sys
import os
import time
import tracemalloc
import random

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "sorting"))
from sorting_algorithms import bubble_sort, insertion_sort, merge_sort, quick_sort

sys.setrecursionlimit(10000)
random.seed(2026)

input_sizes = [100, 500, 1000, 2000]
conditions = ["Random", "Sorted", "Reverse-Sorted"]
algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
}


def generate_data(n, condition):
    if condition == "Random":
        return [random.randint(1, 100000) for _ in range(n)]
    elif condition == "Sorted":
        return list(range(n))
    elif condition == "Reverse-Sorted":
        return list(range(n, 0, -1))


def run_experiment():
    results = []
    for condition in conditions:
        for n in input_sizes:
            base_data = generate_data(n, condition)
            for algo_name, algo_func in algorithms.items():
                arr = base_data.copy()
                counter = [0]

                tracemalloc.start()
                start = time.perf_counter()

                algo_func(arr, counter=counter)

                end = time.perf_counter()
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                results.append({
                    "condition": condition,
                    "size": n,
                    "algorithm": algo_name,
                    "time": end - start,
                    "memory": peak,
                    "comparisons": counter[0],
                })
    return results


def print_results(results):
    header = (f"{'Condition':<16}{'Size':<7}{'Algorithm':<16}{'Time (s)':<13}"
              f"{'Memory (B)':<13}{'Comparisons':<12}")
    print(header)
    print("-" * len(header))
    for r in results:
        print(f"{r['condition']:<16}{r['size']:<7}{r['algorithm']:<16}"
              f"{r['time']:<13.6f}{r['memory']:<13}{r['comparisons']:<12}")


if __name__ == "__main__":
    data = run_experiment()
    print_results(data)
