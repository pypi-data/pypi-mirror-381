"""
Algorithms Package - DSA Toolkit

This package contains implementations of fundamental algorithm paradigms:

- greedy: Greedy algorithm implementations (activity selection, fractional knapsack, 
  huffman coding, job scheduling, minimum spanning tree, etc.)
- divide_and_conquer: Divide and conquer algorithms (enhanced merge sort, quick sort,
  binary search variations, maximum subarray, closest pair, Strassen matrix multiplication)
- dynamic_programming: Dynamic programming solutions (fibonacci, knapsack, LCS, LIS,
  edit distance, coin change, matrix chain multiplication, palindrome problems, grid paths)

Each module includes:
- Multiple approaches (memoization, tabulation, space optimization where applicable)
- Debug mode for step-by-step algorithm tracing
- Comprehensive examples and test cases
- Time and space complexity analysis
- Type hints and detailed docstrings

Example usage:
    from dsa.algorithms import greedy, divide_and_conquer, dynamic_programming
    
    # Greedy algorithm
    activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (8, 9)]
    selected = greedy.activity_selection(activities, debug=True)
    
    # Divide and conquer
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_arr = divide_and_conquer.merge_sort(arr, debug=True)
    
    # Dynamic programming
    result = dynamic_programming.fibonacci_memoization(10, debug=True)
    
    # 0/1 Knapsack
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    max_value, items = dynamic_programming.knapsack_01_tabulation(weights, values, capacity, debug=True)
"""

# Import all modules for easy access
from . import greedy
from . import divide_and_conquer
from . import dynamic_programming

__all__ = [
    'greedy',
    'divide_and_conquer',
    'dynamic_programming'
]
