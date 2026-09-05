"""
DAA Lab - Question 3: Graphs and Visualizations
Generates graphs comparing execution time and memory consumption of
the sorting algorithms (on random data) and the Fibonacci programs.
"""
import sys
import os
import time
import tracemalloc
import random
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.setrecursionlimit(10000)
random.seed(2026)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "sorting"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "fibonacci"))
from sorting_algorithms import bubble_sort, insertion_sort, merge_sort, quick_sort
from fibonacci_recursive import fib_recursive
from fibonacci_iterative import fib_iterative
from fibonacci_memoized import fib_memoized

# ---------------- Sorting: time, memory & comparisons vs input size (random data) ----------------
input_sizes = [100, 500, 1000, 2000, 4000]
algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
}

sort_times = {name: [] for name in algorithms}
sort_memory = {name: [] for name in algorithms}
sort_comparisons = {name: [] for name in algorithms}

for n in input_sizes:
    data = [random.randint(1, 100000) for _ in range(n)]
    for name, func in algorithms.items():
        arr = data.copy()
        counter = [0]
        tracemalloc.start()
        start = time.perf_counter()
        func(arr, counter=counter)
        end = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        sort_times[name].append(end - start)
        sort_memory[name].append(peak / 1024)  # KB
        sort_comparisons[name].append(counter[0])

plt.figure(figsize=(8, 5))
for name in algorithms:
    plt.plot(input_sizes, sort_times[name], marker="o", label=name)
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Sorting Algorithms - Execution Time vs Input Size (Random Data)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("graph_sort_time.png", dpi=130)
plt.close()

plt.figure(figsize=(8, 5))
for name in algorithms:
    plt.plot(input_sizes, sort_memory[name], marker="o", label=name)
plt.xlabel("Input Size (n)")
plt.ylabel("Peak Memory (KB)")
plt.title("Sorting Algorithms - Memory Usage vs Input Size (Random Data)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("graph_sort_memory.png", dpi=130)
plt.close()

plt.figure(figsize=(8, 5))
for name in algorithms:
    plt.plot(input_sizes, sort_comparisons[name], marker="o", label=name)
plt.xlabel("Input Size (n)")
plt.ylabel("Number of Comparisons")
plt.yscale("log")
plt.title("Sorting Algorithms - Comparison Count vs Input Size (Random Data)")
plt.legend()
plt.grid(True, which="both")
plt.tight_layout()
plt.savefig("graph_sort_comparisons.png", dpi=130)
plt.close()

# ---------------- Fibonacci: time & memory vs n ----------------
fib_ns = [5, 10, 15, 20, 25, 30]
fib_funcs = {"Recursive": fib_recursive, "Iterative": fib_iterative, "Memoized": fib_memoized}
fib_times = {name: [] for name in fib_funcs}
fib_memory = {name: [] for name in fib_funcs}

for n in fib_ns:
    for name, func in fib_funcs.items():
        tracemalloc.start()
        start = time.perf_counter()
        func(n)
        end = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        fib_times[name].append(end - start)
        fib_memory[name].append(peak)  # bytes (values are small)

plt.figure(figsize=(8, 5))
for name in fib_funcs:
    plt.plot(fib_ns, fib_times[name], marker="o", label=name)
plt.xlabel("n")
plt.ylabel("Execution Time (seconds)")
plt.title("Fibonacci Programs - Execution Time vs n")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("graph_fib_time.png", dpi=130)
plt.close()

plt.figure(figsize=(8, 5))
for name in fib_funcs:
    plt.plot(fib_ns, fib_memory[name], marker="o", label=name)
plt.xlabel("n")
plt.ylabel("Peak Memory (bytes)")
plt.title("Fibonacci Programs - Memory Usage vs n")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("graph_fib_memory.png", dpi=130)
plt.close()

print("Graphs generated: graph_sort_time.png, graph_sort_memory.png, graph_fib_time.png, graph_fib_memory.png")
