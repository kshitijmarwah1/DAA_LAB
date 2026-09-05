"""
DAA Lab - Question 2: Complexity Comparison Table
Prints best-case, average-case, worst-case, and space complexities
for all implemented algorithms (sorting + Fibonacci).
"""

complexities = [
    ("Bubble Sort",        "O(n)",      "O(n^2)",    "O(n^2)",    "O(1)"),
    ("Insertion Sort",     "O(n)",      "O(n^2)",    "O(n^2)",    "O(1)"),
    ("Merge Sort",         "O(n log n)","O(n log n)","O(n log n)","O(n)"),
    ("Quick Sort",         "O(n log n)","O(n log n)","O(n^2)",    "O(log n)"),
    ("Fibonacci (Recursive)", "O(2^n)", "O(2^n)",    "O(2^n)",    "O(n)"),
    ("Fibonacci (Iterative)", "O(n)",   "O(n)",      "O(n)",      "O(1)"),
    ("Fibonacci (Memoized)",  "O(n)",   "O(n)",      "O(n)",      "O(n)"),
]


def print_table():
    header = f"{'Algorithm':<24}{'Best Case':<14}{'Average Case':<14}{'Worst Case':<14}{'Space':<10}"
    print(header)
    print("-" * len(header))
    for row in complexities:
        print(f"{row[0]:<24}{row[1]:<14}{row[2]:<14}{row[3]:<14}{row[4]:<10}")


if __name__ == "__main__":
    print_table()
