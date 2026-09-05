"""
DAA Lab - Sorting Algorithms
Implements Bubble Sort, Insertion Sort, Merge Sort, and Quick Sort.

Each function accepts an optional `counter` argument - a single-element
list, e.g. [0] - used to tally the number of key comparisons performed.
Pass counter=None (the default) for normal use with no counting overhead.
"""


def bubble_sort(arr, counter=None):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if counter is not None:
                counter[0] += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def insertion_sort(arr, counter=None):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            if counter is not None:
                counter[0] += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr


def merge_sort(arr, counter=None):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left, counter)
        merge_sort(right, counter)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if counter is not None:
                counter[0] += 1
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


def quick_sort(arr, low=0, high=None, counter=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if counter is not None:
                counter[0] += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1

        quick_sort(arr, low, pi - 1, counter)
        quick_sort(arr, pi + 1, high, counter)
    return arr


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]
    print("Original:", sample)
    print("Bubble Sort:", bubble_sort(sample.copy()))
    print("Insertion Sort:", insertion_sort(sample.copy()))
    print("Merge Sort:", merge_sort(sample.copy()))
    print("Quick Sort:", quick_sort(sample.copy()))
