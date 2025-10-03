"""
searching.py - DSA Toolkit

This module implements basic and advanced searching algorithms:
- Linear Search
- Binary Search (Iterative)
- Binary Search (Recursive)
- Jump Search
- Exponential Search
- Interpolation Search
- Linear Search in 2D Array
- Binary Search in Sorted 2D Matrix

All functions support optional debug output for tracing.
"""
import math

def linear_search(arr, target, debug=False):
    """
    Linear Search Algorithm.
    """
    for i, val in enumerate(arr):
        if debug:
            print(f"Checking index {i}: {val}")
        if val == target:
            return i
    return -1

def binary_search_iterative(arr, target, debug=False):
    """
    Binary Search (Iterative).
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if debug:
            print(f"Left: {left}, Right: {right}, Mid: {mid}, MidValue: {arr[mid]}")
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_recursive(arr, target, left=0, right=None, debug=False):
    """
    Binary Search (Recursive).
    """
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if debug:
        print(f"Left: {left}, Right: {right}, Mid: {mid}, MidValue: {arr[mid]}")
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, debug)
    else:
        return binary_search_recursive(arr, target, left, mid - 1, debug)

def jump_search(arr, target, debug=False):
    """
    Jump Search - works on sorted arrays.
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while prev < n and arr[min(step, n)-1] < target:
        if debug:
            print(f"Jumping from {prev} to {min(step, n)-1}")
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if debug:
            print(f"Checking index {i}: {arr[i]}")
        if arr[i] == target:
            return i
    return -1

def exponential_search(arr, target, debug=False):
    """
    Exponential Search - fast for unbounded sorted arrays.
    """
    if len(arr) == 0:
        return -1
    if arr[0] == target:
        return 0
    index = 1
    while index < len(arr) and arr[index] <= target:
        if debug:
            print(f"Exponential index: {index}, value: {arr[index]}")
        index *= 2
    return binary_search_recursive(arr, target, index // 2, min(index, len(arr)-1), debug)

def interpolation_search(arr, target, debug=False):
    """
    Interpolation Search - works best when data is uniformly distributed.
    """
    low = 0
    high = len(arr) - 1
    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        pos = low + ((high - low) * (target - arr[low]) // (arr[high] - arr[low]))
        if pos >= len(arr):
            return -1
        if debug:
            print(f"Low: {low}, High: {high}, Pos: {pos}, Value: {arr[pos]}")
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

def linear_search_2d(matrix, target, debug=False):
    """
    Linear Search in a 2D array.
    """
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if debug:
                print(f"Checking matrix[{i}][{j}] = {val}")
            if val == target:
                return (i, j)
    return -1

def binary_search_2d(matrix, target, debug=False):
    """
    Binary Search in a 2D matrix with sorted rows and increasing order across rows.
    """
    if not matrix or not matrix[0]:
        return -1
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = (left + right) // 2
        i, j = divmod(mid, cols)
        if debug:
            print(f"Left: {left}, Right: {right}, Mid: {mid} -> matrix[{i}][{j}] = {matrix[i][j]}")
        if matrix[i][j] == target:
            return (i, j)
        elif matrix[i][j] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Sample usage:
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print("\nLinear Search (target=7):", linear_search(arr, 7, debug=True))
    print("\nBinary Search Iterative (target=9):", binary_search_iterative(arr, 9, debug=True))
    print("\nBinary Search Recursive (target=3):", binary_search_recursive(arr, 3, debug=True))
    print("\nJump Search (target=11):", jump_search(arr, 11, debug=True))
    print("\nExponential Search (target=13):", exponential_search(arr, 13, debug=True))
    print("\nInterpolation Search (target=15):", interpolation_search(arr, 15, debug=True))

    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    print("\nLinear Search in 2D (target=9):", linear_search_2d(matrix, 9, debug=True))
    print("\nBinary Search in 2D (target=13):", binary_search_2d(matrix, 13, debug=True))
