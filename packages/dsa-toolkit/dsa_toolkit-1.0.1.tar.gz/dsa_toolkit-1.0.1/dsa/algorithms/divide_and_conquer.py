"""
divide_and_conquer.py - DSA Toolkit

This module implements classic divide and conquer algorithms:
- Merge Sort and Quick Sort (advanced implementations)
- Binary Search variations
- Maximum Subarray (Kadane's Algorithm)
- Closest Pair of Points
- Strassen's Matrix Multiplication
- Fast Exponentiation
- Count Inversions
- Convex Hull (Graham Scan)

Features:
- Comprehensive divide and conquer implementations
- Step-by-step debug tracing
- Time complexity analysis
- Real-world applications
"""

from typing import List, Tuple, Optional, Any
import math
import random


# ============================================================================
# MERGE SORT (ENHANCED VERSION)
# ============================================================================

def merge_sort(arr: List[Any], debug: bool = False, depth: int = 0) -> List[Any]:
    """
    Enhanced Merge Sort with detailed tracing.
    
    Args:
        arr: List to sort
        debug: Enable debug output
        depth: Current recursion depth (for formatting)
    
    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr.copy()
    
    indent = "  " * depth
    mid = len(arr) // 2
    
    if debug:
        print(f"{indent}Dividing: {arr} -> {arr[:mid]} | {arr[mid:]}")
    
    left = merge_sort(arr[:mid], debug, depth + 1)
    right = merge_sort(arr[mid:], debug, depth + 1)
    
    # Merge process
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
    
    # Add remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    if debug:
        print(f"{indent}Result: {merged}")
    
    return merged


def merge_sort_inplace(arr: List[Any], left: int = 0, right: int = None, debug: bool = False, depth: int = 0) -> None:
    """
    In-place merge sort implementation.
    
    Args:
        arr: List to sort (modified in-place)
        left: Left boundary
        right: Right boundary
        debug: Enable debug output
        depth: Current recursion depth
    """
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        mid = (left + right) // 2
        indent = "  " * depth
        
        if debug:
            print(f"{indent}Dividing: arr[{left}:{right+1}] = {arr[left:right+1]}")
        
        merge_sort_inplace(arr, left, mid, debug, depth + 1)
        merge_sort_inplace(arr, mid + 1, right, debug, depth + 1)
        merge_inplace(arr, left, mid, right, debug, depth)


def merge_inplace(arr: List[Any], left: int, mid: int, right: int, debug: bool = False, depth: int = 0) -> None:
    """Helper function for in-place merge."""
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]
    
    i = j = 0
    k = left
    indent = "  " * depth
    
    if debug:
        print(f"{indent}Merging: {left_arr} + {right_arr}")
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    
    if debug:
        print(f"{indent}Merged result: {arr[left:right+1]}")


# ============================================================================
# QUICK SORT (ENHANCED VERSION)
# ============================================================================

def quick_sort(arr: List[Any], debug: bool = False, depth: int = 0) -> List[Any]:
    """
    Enhanced Quick Sort with randomized pivot.
    
    Args:
        arr: List to sort
        debug: Enable debug output
        depth: Current recursion depth
    
    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr.copy()
    
    # Randomized pivot selection
    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]
    
    indent = "  " * depth
    if debug:
        print(f"{indent}Quick Sort: {arr}, pivot = {pivot} (index {pivot_idx})")
    
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    
    if debug:
        print(f"{indent}Partitioned: less={less}, equal={equal}, greater={greater}")
    
    sorted_less = quick_sort(less, debug, depth + 1)
    sorted_greater = quick_sort(greater, debug, depth + 1)
    
    result = sorted_less + equal + sorted_greater
    
    if debug:
        print(f"{indent}Result: {result}")
    
    return result


def quick_sort_inplace(arr: List[Any], low: int = 0, high: int = None, debug: bool = False, depth: int = 0) -> None:
    """
    In-place Quick Sort with Lomuto partition.
    
    Args:
        arr: List to sort (modified in-place)
        low: Low index
        high: High index
        debug: Enable debug output
        depth: Current recursion depth
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Randomized pivot
        random_idx = random.randint(low, high)
        arr[random_idx], arr[high] = arr[high], arr[random_idx]
        
        pi = lomuto_partition(arr, low, high, debug, depth)
        
        quick_sort_inplace(arr, low, pi - 1, debug, depth + 1)
        quick_sort_inplace(arr, pi + 1, high, debug, depth + 1)


def lomuto_partition(arr: List[Any], low: int, high: int, debug: bool = False, depth: int = 0) -> int:
    """Lomuto partition scheme for Quick Sort."""
    pivot = arr[high]
    i = low - 1
    indent = "  " * depth
    
    if debug:
        print(f"{indent}Partitioning: {arr[low:high+1]}, pivot = {pivot}")
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            if debug:
                print(f"{indent}Swapped: {arr[j]} ↔ {arr[i]} -> {arr[low:high+1]}")
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    if debug:
        print(f"{indent}Final partition: {arr[low:high+1]}, pivot at index {i + 1}")
    
    return i + 1


# ============================================================================
# BINARY SEARCH VARIATIONS
# ============================================================================

def binary_search_recursive(arr: List[Any], target: Any, left: int = 0, right: int = None, debug: bool = False, depth: int = 0) -> int:
    """
    Recursive binary search implementation.
    
    Args:
        arr: Sorted list to search
        target: Element to find
        left: Left boundary
        right: Right boundary
        debug: Enable debug output
        depth: Current recursion depth
    
    Returns:
        Index of target, or -1 if not found
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        if debug:
            print("  " * depth + f"Target {target} not found")
        return -1
    
    mid = (left + right) // 2
    indent = "  " * depth
    
    if debug:
        print(f"{indent}Binary Search: arr[{left}:{right+1}], mid={mid}, arr[mid]={arr[mid]}")
    
    if arr[mid] == target:
        if debug:
            print(f"{indent}Found {target} at index {mid}")
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1, debug, depth + 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right, debug, depth + 1)


def find_first_occurrence(arr: List[Any], target: Any, debug: bool = False) -> int:
    """Find the first occurrence of target in sorted array with duplicates."""
    left, right = 0, len(arr) - 1
    result = -1
    
    if debug:
        print(f"Finding first occurrence of {target} in {arr}")
    
    while left <= right:
        mid = (left + right) // 2
        
        if debug:
            print(f"Left: {left}, Right: {right}, Mid: {mid}, arr[mid]: {arr[mid]}")
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left
            if debug:
                print(f"Found {target} at {mid}, searching left for first occurrence")
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    if debug:
        print(f"First occurrence at index: {result}")
    
    return result


def find_last_occurrence(arr: List[Any], target: Any, debug: bool = False) -> int:
    """Find the last occurrence of target in sorted array with duplicates."""
    left, right = 0, len(arr) - 1
    result = -1
    
    if debug:
        print(f"Finding last occurrence of {target} in {arr}")
    
    while left <= right:
        mid = (left + right) // 2
        
        if debug:
            print(f"Left: {left}, Right: {right}, Mid: {mid}, arr[mid]: {arr[mid]}")
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right
            if debug:
                print(f"Found {target} at {mid}, searching right for last occurrence")
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    if debug:
        print(f"Last occurrence at index: {result}")
    
    return result


# ============================================================================
# MAXIMUM SUBARRAY (DIVIDE AND CONQUER)
# ============================================================================

def max_subarray_divide_conquer(arr: List[int], debug: bool = False, depth: int = 0) -> Tuple[int, int, int]:
    """
    Maximum subarray problem using divide and conquer.
    
    Args:
        arr: Input array
        debug: Enable debug output
        depth: Current recursion depth
    
    Returns:
        Tuple of (max_sum, start_index, end_index)
    """
    if len(arr) == 1:
        return arr[0], 0, 0
    
    mid = len(arr) // 2
    indent = "  " * depth
    
    if debug:
        print(f"{indent}Max Subarray: {arr}, mid = {mid}")
    
    # Left half
    left_sum, left_start, left_end = max_subarray_divide_conquer(arr[:mid], debug, depth + 1)
    
    # Right half
    right_sum, right_start, right_end = max_subarray_divide_conquer(arr[mid:], debug, depth + 1)
    right_start += mid
    right_end += mid
    
    # Cross middle
    cross_sum, cross_start, cross_end = max_crossing_subarray(arr, 0, mid, len(arr) - 1, debug, depth)
    
    if debug:
        print(f"{indent}Left: sum={left_sum}, indices=({left_start},{left_end})")
        print(f"{indent}Right: sum={right_sum}, indices=({right_start},{right_end})")
        print(f"{indent}Cross: sum={cross_sum}, indices=({cross_start},{cross_end})")
    
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_sum, left_start, left_end
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_sum, right_start, right_end
    else:
        return cross_sum, cross_start, cross_end


def max_crossing_subarray(arr: List[int], low: int, mid: int, high: int, debug: bool = False, depth: int = 0) -> Tuple[int, int, int]:
    """Find maximum subarray that crosses the middle point."""
    left_sum = float('-inf')
    current_sum = 0
    max_left = mid
    
    # Find maximum sum for left side
    for i in range(mid, low - 1, -1):
        current_sum += arr[i]
        if current_sum > left_sum:
            left_sum = current_sum
            max_left = i
    
    right_sum = float('-inf')
    current_sum = 0
    max_right = mid + 1
    
    # Find maximum sum for right side
    for i in range(mid + 1, high + 1):
        current_sum += arr[i]
        if current_sum > right_sum:
            right_sum = current_sum
            max_right = i
    
    cross_sum = left_sum + right_sum
    
    if debug:
        indent = "  " * depth
        print(f"{indent}Cross subarray: arr[{max_left}:{max_right+1}] = {arr[max_left:max_right+1]}, sum = {cross_sum}")
    
    return cross_sum, max_left, max_right


# ============================================================================
# CLOSEST PAIR OF POINTS
# ============================================================================

def closest_pair_points(points: List[Tuple[float, float]], debug: bool = False) -> Tuple[float, Tuple[Tuple[float, float], Tuple[float, float]]]:
    """
    Find closest pair of points using divide and conquer.
    
    Args:
        points: List of (x, y) coordinate tuples
        debug: Enable debug output
    
    Returns:
        Tuple of (minimum_distance, (point1, point2))
    """
    def distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
    def closest_pair_rec(px: List[Tuple[float, float]], py: List[Tuple[float, float]], depth: int = 0) -> Tuple[float, Tuple[Tuple[float, float], Tuple[float, float]]]:
        n = len(px)
        indent = "  " * depth
        
        if debug:
            print(f"{indent}Closest pair for {n} points: {px}")
        
        # Base case: brute force for small arrays
        if n <= 3:
            min_dist = float('inf')
            closest_points = None
            
            for i in range(n):
                for j in range(i + 1, n):
                    dist = distance(px[i], px[j])
                    if dist < min_dist:
                        min_dist = dist
                        closest_points = (px[i], px[j])
            
            if debug:
                print(f"{indent}Brute force result: distance={min_dist:.3f}, points={closest_points}")
            
            return min_dist, closest_points
        
        # Divide
        mid = n // 2
        midpoint = px[mid]
        
        pyl = [point for point in py if point[0] <= midpoint[0]]
        pyr = [point for point in py if point[0] > midpoint[0]]
        
        # Conquer
        dl, pair_l = closest_pair_rec(px[:mid], pyl, depth + 1)
        dr, pair_r = closest_pair_rec(px[mid:], pyr, depth + 1)
        
        # Find minimum of the two
        if dl <= dr:
            d = dl
            closest_points = pair_l
        else:
            d = dr
            closest_points = pair_r
        
        # Find closest points across the divide
        strip = [point for point in py if abs(point[0] - midpoint[0]) < d]
        
        if debug:
            print(f"{indent}Strip points within distance {d:.3f}: {strip}")
        
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and (strip[j][1] - strip[i][1]) < d:
                dist = distance(strip[i], strip[j])
                if dist < d:
                    d = dist
                    closest_points = (strip[i], strip[j])
                    if debug:
                        print(f"{indent}New closest pair found: distance={d:.3f}, points={closest_points}")
                j += 1
        
        return d, closest_points
    
    if len(points) < 2:
        return 0.0, (None, None)
    
    # Sort points by x and y coordinates
    px = sorted(points)
    py = sorted(points, key=lambda p: p[1])
    
    if debug:
        print(f"Finding closest pair among {len(points)} points")
    
    return closest_pair_rec(px, py)


# ============================================================================
# FAST EXPONENTIATION
# ============================================================================

def fast_exponentiation(base: int, exp: int, mod: Optional[int] = None, debug: bool = False, depth: int = 0) -> int:
    """
    Fast exponentiation using divide and conquer.
    
    Args:
        base: Base number
        exp: Exponent
        mod: Optional modulus for modular exponentiation
        debug: Enable debug output
        depth: Current recursion depth
    
    Returns:
        base^exp (mod mod if provided)
    """
    indent = "  " * depth
    
    if debug:
        if mod:
            print(f"{indent}Computing {base}^{exp} mod {mod}")
        else:
            print(f"{indent}Computing {base}^{exp}")
    
    if exp == 0:
        result = 1
    elif exp == 1:
        result = base
    elif exp % 2 == 0:
        # Even exponent: base^exp = (base^(exp/2))^2
        half_result = fast_exponentiation(base, exp // 2, mod, debug, depth + 1)
        result = half_result * half_result
    else:
        # Odd exponent: base^exp = base * base^(exp-1)
        result = base * fast_exponentiation(base, exp - 1, mod, debug, depth + 1)
    
    if mod:
        result %= mod
    
    if debug:
        print(f"{indent}Result: {result}")
    
    return result


# ============================================================================
# COUNT INVERSIONS
# ============================================================================

def count_inversions(arr: List[int], debug: bool = False, depth: int = 0) -> Tuple[List[int], int]:
    """
    Count inversions in array using divide and conquer.
    An inversion is when arr[i] > arr[j] for i < j.
    
    Args:
        arr: Input array
        debug: Enable debug output
        depth: Current recursion depth
    
    Returns:
        Tuple of (sorted_array, inversion_count)
    """
    if len(arr) <= 1:
        return arr.copy(), 0
    
    mid = len(arr) // 2
    indent = "  " * depth
    
    if debug:
        print(f"{indent}Count inversions: {arr}")
    
    left_sorted, left_inv = count_inversions(arr[:mid], debug, depth + 1)
    right_sorted, right_inv = count_inversions(arr[mid:], debug, depth + 1)
    
    merged, split_inv = merge_and_count(left_sorted, right_sorted, debug, depth)
    
    total_inv = left_inv + right_inv + split_inv
    
    if debug:
        print(f"{indent}Total inversions: {left_inv} + {right_inv} + {split_inv} = {total_inv}")
    
    return merged, total_inv


def merge_and_count(left: List[int], right: List[int], debug: bool = False, depth: int = 0) -> Tuple[List[int], int]:
    """Merge two sorted arrays and count split inversions."""
    merged = []
    i = j = 0
    inv_count = 0
    indent = "  " * depth
    
    if debug:
        print(f"{indent}Merging and counting: {left} + {right}")
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            # All remaining elements in left are greater than right[j]
            inv_count += len(left) - i
            j += 1
            if debug:
                print(f"{indent}Inversion found: {len(left) - i} elements in left > {right[j-1]}")
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    if debug:
        print(f"{indent}Merge result: {merged}, split inversions: {inv_count}")
    
    return merged, inv_count


# ============================================================================
# MATRIX MULTIPLICATION (STRASSEN'S ALGORITHM)
# ============================================================================

def matrix_multiply_strassen(A: List[List[int]], B: List[List[int]], debug: bool = False) -> List[List[int]]:
    """
    Strassen's algorithm for matrix multiplication.
    
    Args:
        A: First matrix (n x n)
        B: Second matrix (n x n)
        debug: Enable debug output
    
    Returns:
        Product matrix C = A * B
    """
    n = len(A)
    
    # Base case: 1x1 matrix
    if n == 1:
        result = [[A[0][0] * B[0][0]]]
        if debug:
            print(f"Base case: {A[0][0]} * {B[0][0]} = {result[0][0]}")
        return result
    
    # Pad matrices to next power of 2 if needed
    next_power = 1
    while next_power < n:
        next_power *= 2
    
    if next_power != n:
        A = pad_matrix(A, next_power)
        B = pad_matrix(B, next_power)
        n = next_power
    
    if debug:
        print(f"Strassen multiplication for {n}x{n} matrices")
    
    # Divide matrices into quadrants
    mid = n // 2
    
    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]
    
    B11 = [[B[i][j] for j in range(mid)] for i in range(mid)]
    B12 = [[B[i][j] for j in range(mid, n)] for i in range(mid)]
    B21 = [[B[i][j] for j in range(mid)] for i in range(mid, n)]
    B22 = [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]
    
    # Strassen's 7 multiplications
    M1 = matrix_multiply_strassen(matrix_add(A11, A22), matrix_add(B11, B22), debug)
    M2 = matrix_multiply_strassen(matrix_add(A21, A22), B11, debug)
    M3 = matrix_multiply_strassen(A11, matrix_subtract(B12, B22), debug)
    M4 = matrix_multiply_strassen(A22, matrix_subtract(B21, B11), debug)
    M5 = matrix_multiply_strassen(matrix_add(A11, A12), B22, debug)
    M6 = matrix_multiply_strassen(matrix_subtract(A21, A11), matrix_add(B11, B12), debug)
    M7 = matrix_multiply_strassen(matrix_subtract(A12, A22), matrix_add(B21, B22), debug)
    
    # Combine results
    C11 = matrix_add(matrix_subtract(matrix_add(M1, M4), M5), M7)
    C12 = matrix_add(M3, M5)
    C21 = matrix_add(M2, M4)
    C22 = matrix_add(matrix_subtract(matrix_add(M1, M3), M2), M6)
    
    # Combine quadrants
    C = [[0] * n for _ in range(n)]
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]
    
    # Remove padding if it was added
    if len(C) != len(A):
        C = [[C[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    
    return C


def matrix_add(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """Add two matrices."""
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


def matrix_subtract(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """Subtract two matrices."""
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


def pad_matrix(matrix: List[List[int]], size: int) -> List[List[int]]:
    """Pad matrix with zeros to reach specified size."""
    n = len(matrix)
    padded = [[0] * size for _ in range(size)]
    for i in range(n):
        for j in range(len(matrix[0])):
            padded[i][j] = matrix[i][j]
    return padded


# ============================================================================
# EXAMPLE USAGE AND TESTING
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("Divide and Conquer Algorithms Demo")
    print("=" * 70)
    
    # 1. Enhanced Merge Sort
    print("\n1. Enhanced Merge Sort:")
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {arr}")
    sorted_arr = merge_sort(arr, debug=True)
    print(f"Sorted: {sorted_arr}")
    
    # 2. Binary Search Variations
    print("\n2. Binary Search Variations:")
    sorted_arr = [1, 2, 2, 3, 3, 3, 4, 5, 5]
    target = 3
    print(f"Array: {sorted_arr}, Target: {target}")
    
    first = find_first_occurrence(sorted_arr, target, debug=True)
    last = find_last_occurrence(sorted_arr, target, debug=True)
    print(f"First occurrence: {first}, Last occurrence: {last}")
    
    # 3. Maximum Subarray
    print("\n3. Maximum Subarray Problem:")
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum, start, end = max_subarray_divide_conquer(arr, debug=True)
    print(f"Maximum subarray: arr[{start}:{end+1}] = {arr[start:end+1]}, sum = {max_sum}")
    
    # 4. Closest Pair of Points
    print("\n4. Closest Pair of Points:")
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    min_dist, closest = closest_pair_points(points, debug=True)
    print(f"Closest pair: {closest[0]} and {closest[1]}, distance = {min_dist:.3f}")
    
    # 5. Fast Exponentiation
    print("\n5. Fast Exponentiation:")
    base, exp = 3, 10
    result = fast_exponentiation(base, exp, debug=True)
    print(f"{base}^{exp} = {result}")
    
    # Modular exponentiation
    mod = 1000
    result_mod = fast_exponentiation(base, exp, mod, debug=True)
    print(f"{base}^{exp} mod {mod} = {result_mod}")
    
    # 6. Count Inversions
    print("\n6. Count Inversions:")
    arr = [2, 3, 8, 6, 1]
    sorted_arr, inv_count = count_inversions(arr, debug=True)
    print(f"Array: {arr}")
    print(f"Number of inversions: {inv_count}")
    print(f"Sorted array: {sorted_arr}")
    
    # 7. Matrix Multiplication (Strassen)
    print("\n7. Strassen's Matrix Multiplication:")
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    
    print(f"Matrix A: {A}")
    print(f"Matrix B: {B}")
    
    C = matrix_multiply_strassen(A, B, debug=True)
    print(f"A * B = {C}")
    
    # Verify with standard multiplication
    def standard_multiply(A, B):
        n = len(A)
        C = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    C[i][j] += A[i][k] * B[k][j]
        return C
    
    C_standard = standard_multiply(A, B)
    print(f"Verification (standard): {C_standard}")
    print(f"Results match: {C == C_standard}")
