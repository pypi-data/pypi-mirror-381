"""
📦 sorting.py - Part of dsa_toolkit package

Includes common sorting algorithms:
1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Merge Sort
5. Quick Sort

Each function accepts:
- arr: List of elements to sort
- debug (bool): If True, prints step-by-step operations

All functions return a **new sorted list** (original is not modified).
"""

# -----------------------------------------------
# 1. Bubble Sort
# -----------------------------------------------

def bubble_sort(arr, debug=False):
    """Bubble Sort: Repeatedly swaps adjacent elements if they are in the wrong order."""
    n = len(arr)
    arr = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if debug:
                print(f"Comparing {arr[j]} and {arr[j+1]}")
            if arr[j] > arr[j + 1]:
                if debug:
                    print(f"Swapping {arr[j]} and {arr[j+1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if debug:
            print(f"Pass {i+1}: {arr}")
    return arr


# -----------------------------------------------
# 2. Selection Sort
# -----------------------------------------------

def selection_sort(arr, debug=False):
    """Selection Sort: Selects the smallest element and puts it at the correct position."""
    n = len(arr)
    arr = arr.copy()
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if debug:
                print(f"Comparing {arr[j]} and {arr[min_idx]}")
            if arr[j] < arr[min_idx]:
                min_idx = j
        if debug:
            print(f"Swapping {arr[i]} and {arr[min_idx]}")
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        if debug:
            print(f"After iteration {i+1}: {arr}")
    return arr


# -----------------------------------------------
# 3. Insertion Sort
# -----------------------------------------------

def insertion_sort(arr, debug=False):
    """Insertion Sort: Builds sorted array by inserting elements one by one."""
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        if debug:
            print(f"Inserting {key}")
        while j >= 0 and key < arr[j]:
            if debug:
                print(f"Moving {arr[j]} to position {j+1}")
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        if debug:
            print(f"After inserting {key}: {arr}")
    return arr


# -----------------------------------------------
# 4. Merge Sort
# -----------------------------------------------

def merge_sort(arr, debug=False, depth=0):
    """Merge Sort: Divide-and-conquer algorithm that recursively splits and merges."""
    indent = "  " * depth
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    if debug:
        print(f"{indent}Dividing: {arr[:mid]} | {arr[mid:]}")

    left = merge_sort(arr[:mid], debug, depth + 1)
    right = merge_sort(arr[mid:], debug, depth + 1)

    merged = []
    i = j = 0

    if debug:
        print(f"{indent}Merging: {left} + {right}")

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    if debug:
        print(f"{indent}Result: {merged}")

    return merged


# -----------------------------------------------
# 5. Quick Sort (Lomuto Partition)
# -----------------------------------------------

def quick_sort(arr, debug=False, depth=0):
    """Quick Sort: Picks a pivot and partitions array around it recursively."""

    def _quick_sort(arr, low, high, depth):
        if low < high:
            pi = partition(arr, low, high, depth)
            _quick_sort(arr, low, pi - 1, depth + 1)
            _quick_sort(arr, pi + 1, high, depth + 1)

    def partition(arr, low, high, depth):
        indent = "  " * depth
        pivot = arr[high]
        i = low - 1
        if debug:
            print(f"{indent}Pivot: {pivot} | Subarray: {arr[low:high+1]}")
        for j in range(low, high):
            if debug:
                print(f"{indent}Comparing {arr[j]} with {pivot}")
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                if debug:
                    print(f"{indent}Swapped: {arr[i]} and {arr[j]} → {arr}")
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        if debug:
            print(f"{indent}Moved Pivot: {arr[i + 1]} → {arr}")
        return i + 1

    arr = arr.copy()
    _quick_sort(arr, 0, len(arr) - 1, depth)
    return arr

# -----------------------------------------------
# 6. Counting Sort
# -----------------------------------------------

def counting_sort(arr, debug=False):
    """Counting Sort: Non-comparison sort for integers in a known small range."""
    if not arr:
        return []

    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1
    count = [0] * range_size
    output = [0] * len(arr)

    for num in arr:
        count[num - min_val] += 1
        if debug:
            print(f"Counting {num}: {count}")

    for i in range(1, len(count)):
        count[i] += count[i - 1]
    if debug:
        print(f"Cumulative Count: {count}")

    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
        if debug:
            print(f"Placing {num}: {output}")

    return output

# -----------------------------------------------
# 7. Radix Sort (LSD)
# -----------------------------------------------

def radix_sort(arr, debug=False):
    """Radix Sort: Sorts numbers digit by digit (Least Significant Digit)."""
    def counting_sort_by_digit(arr, exp, debug):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for num in arr:
            index = (num // exp) % 10
            count[index] += 1
        if debug:
            print(f"Digit count at exp={exp}: {count}")

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in reversed(range(n)):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
        if debug:
            print(f"After exp={exp}, pass result: {output}")

        return output

    if not arr:
        return []

    max_num = max(arr)
    exp = 1
    sorted_arr = arr.copy()
    while max_num // exp > 0:
        sorted_arr = counting_sort_by_digit(sorted_arr, exp, debug)
        exp *= 10

    return sorted_arr

# -----------------------------------------------
# 8. Heap Sort
# -----------------------------------------------

def heap_sort(arr, debug=False):
    """Heap Sort: Converts list to heap and sorts by extracting max repeatedly."""

    def heapify(arr, n, i, debug):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            if debug:
                print(f"Swapping {arr[i]} and {arr[largest]}")
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest, debug)

    arr = arr.copy()
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, debug)

    for i in range(n - 1, 0, -1):
        if debug:
            print(f"Swapping {arr[0]} and {arr[i]}")
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, debug)

    return arr

# -----------------------------------------------
# 9. Shell Sort
# -----------------------------------------------

def shell_sort(arr, debug=False):
    """Shell Sort: Optimized Insertion Sort using gap sequence."""
    arr = arr.copy()
    n = len(arr)
    gap = n // 2

    while gap > 0:
        if debug:
            print(f"Gap: {gap}")
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                if debug:
                    print(f"Shifting {arr[j-gap]} to {j}")
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
            if debug:
                print(f"After inserting {temp}: {arr}")
        gap //= 2

    return arr


# -----------------------------------------------
# Example usage for testing
# -----------------------------------------------

if __name__ == "__main__":
    sample = [64, 25, 12, 22, 11]

    print("\nBubble Sort:")
    print(bubble_sort(sample, debug=True))

    print("\nSelection Sort:")
    print(selection_sort(sample, debug=True))

    print("\nInsertion Sort:")
    print(insertion_sort(sample, debug=True))

    print("\nMerge Sort:")
    print(merge_sort(sample, debug=True))

    print("\nQuick Sort:")
    print(quick_sort(sample, debug=True))

    print("\nCounting Sort:")
    print(counting_sort(sample, debug=True))

    print("\nRadix Sort:")
    print(radix_sort(sample, debug=True))

    print("\nHeap Sort:")
    print(heap_sort(sample, debug=True))

    print("\nShell Sort:")
    print(shell_sort(sample, debug=True))
