"""
dynamic_programming.py - DSA Toolkit

This module implements classic dynamic programming algorithms:
- Fibonacci (Memoization & Tabulation)
- 0/1 Knapsack Problem
- Longest Common Subsequence (LCS)
- Longest Increasing Subsequence (LIS)
- Edit Distance (Levenshtein)
- Coin Change Problem
- Matrix Chain Multiplication
- Palindrome Problems
- Grid Path Problems

Features:
- Both memoization (top-down) and tabulation (bottom-up) approaches
- Step-by-step debug tracing
- Space and time complexity optimizations
- Real-world applications
"""

from typing import List, Tuple, Dict, Optional, Any
import functools


# ============================================================================
# FIBONACCI SEQUENCE (MULTIPLE APPROACHES)
# ============================================================================

def fibonacci_memoization(n: int, memo: Dict[int, int] = None, debug: bool = False, depth: int = 0) -> int:
    """
    Fibonacci using memoization (top-down DP).
    
    Args:
        n: The nth Fibonacci number to compute
        memo: Memoization cache
        debug: Enable debug output
        depth: Current recursion depth
    
    Returns:
        The nth Fibonacci number
    """
    if memo is None:
        memo = {}
    
    indent = "  " * depth
    
    if debug:
        print(f"{indent}fibonacci_memo({n})")
    
    if n in memo:
        if debug:
            print(f"{indent}Cache hit: F({n}) = {memo[n]}")
        return memo[n]
    
    if n <= 1:
        memo[n] = n
        return n
    
    memo[n] = fibonacci_memoization(n-1, memo, debug, depth+1) + fibonacci_memoization(n-2, memo, debug, depth+1)
    
    if debug:
        print(f"{indent}Computed: F({n}) = {memo[n]}")
    
    return memo[n]


def fibonacci_tabulation(n: int, debug: bool = False) -> int:
    """
    Fibonacci using tabulation (bottom-up DP).
    
    Args:
        n: The nth Fibonacci number to compute
        debug: Enable debug output
    
    Returns:
        The nth Fibonacci number
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    if debug:
        print(f"Fibonacci tabulation for F({n}):")
        print(f"dp[0] = {dp[0]}, dp[1] = {dp[1]}")
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        if debug:
            print(f"dp[{i}] = dp[{i-1}] + dp[{i-2}] = {dp[i-1]} + {dp[i-2]} = {dp[i]}")
    
    return dp[n]


def fibonacci_space_optimized(n: int, debug: bool = False) -> int:
    """
    Space-optimized Fibonacci using only two variables.
    
    Args:
        n: The nth Fibonacci number to compute
        debug: Enable debug output
    
    Returns:
        The nth Fibonacci number
    """
    if n <= 1:
        return n
    
    prev2 = 0  # F(0)
    prev1 = 1  # F(1)
    
    if debug:
        print(f"Space-optimized Fibonacci for F({n}):")
        print(f"F(0) = {prev2}, F(1) = {prev1}")
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        if debug:
            print(f"F({i}) = F({i-1}) + F({i-2}) = {prev1} + {prev2} = {current}")
        prev2 = prev1
        prev1 = current
    
    return prev1


# ============================================================================
# 0/1 KNAPSACK PROBLEM
# ============================================================================

def knapsack_01_memoization(weights: List[int], values: List[int], capacity: int, debug: bool = False) -> Tuple[int, List[int]]:
    """
    0/1 Knapsack using memoization.
    
    Args:
        weights: List of item weights
        values: List of item values
        capacity: Knapsack capacity
        debug: Enable debug output
    
    Returns:
        Tuple of (max_value, selected_items_indices)
    """
    n = len(weights)
    memo = {}
    
    def knapsack_recursive(i: int, w: int, depth: int = 0) -> int:
        indent = "  " * depth
        
        if debug:
            print(f"{indent}knapsack({i}, {w})")
        
        if (i, w) in memo:
            if debug:
                print(f"{indent}Cache hit: ({i}, {w}) = {memo[(i, w)]}")
            return memo[(i, w)]
        
        if i == 0 or w == 0:
            memo[(i, w)] = 0
            return 0
        
        if weights[i-1] <= w:
            # Choose the maximum of including or excluding current item
            include = values[i-1] + knapsack_recursive(i-1, w - weights[i-1], depth+1)
            exclude = knapsack_recursive(i-1, w, depth+1)
            memo[(i, w)] = max(include, exclude)
            
            if debug:
                print(f"{indent}Item {i-1}: weight={weights[i-1]}, value={values[i-1]}")
                print(f"{indent}Include: {values[i-1]} + {include - values[i-1]} = {include}")
                print(f"{indent}Exclude: {exclude}")
                print(f"{indent}Max: {memo[(i, w)]}")
        else:
            memo[(i, w)] = knapsack_recursive(i-1, w, depth+1)
            if debug:
                print(f"{indent}Item {i-1} too heavy, exclude")
        
        return memo[(i, w)]
    
    max_value = knapsack_recursive(n, capacity)
    
    # Backtrack to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if memo.get((i, w), 0) != memo.get((i-1, w), 0):
            selected.append(i-1)
            w -= weights[i-1]
    
    selected.reverse()
    
    if debug:
        print(f"Selected items: {selected}")
        print(f"Total value: {max_value}")
    
    return max_value, selected


def knapsack_01_tabulation(weights: List[int], values: List[int], capacity: int, debug: bool = False) -> Tuple[int, List[int]]:
    """
    0/1 Knapsack using tabulation.
    
    Args:
        weights: List of item weights
        values: List of item values
        capacity: Knapsack capacity
        debug: Enable debug output
    
    Returns:
        Tuple of (max_value, selected_items_indices)
    """
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    if debug:
        print(f"0/1 Knapsack tabulation:")
        print(f"Items: {list(zip(weights, values))}")
        print(f"Capacity: {capacity}")
    
    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                include = values[i-1] + dp[i-1][w - weights[i-1]]
                exclude = dp[i-1][w]
                dp[i][w] = max(include, exclude)
                
                if debug and dp[i][w] > dp[i-1][w]:
                    print(f"dp[{i}][{w}] = max({include}, {exclude}) = {dp[i][w]} (include item {i-1})")
            else:
                dp[i][w] = dp[i-1][w]
    
    # Backtrack to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i-1)
            w -= weights[i-1]
    
    selected.reverse()
    
    if debug:
        print(f"DP table:")
        for row in dp:
            print(row)
        print(f"Selected items: {selected}")
        print(f"Maximum value: {dp[n][capacity]}")
    
    return dp[n][capacity], selected


# ============================================================================
# LONGEST COMMON SUBSEQUENCE (LCS)
# ============================================================================

def lcs_memoization(text1: str, text2: str, debug: bool = False) -> Tuple[int, str]:
    """
    Longest Common Subsequence using memoization.
    
    Args:
        text1: First string
        text2: Second string
        debug: Enable debug output
    
    Returns:
        Tuple of (lcs_length, lcs_string)
    """
    memo = {}
    
    def lcs_recursive(i: int, j: int, depth: int = 0) -> int:
        indent = "  " * depth
        
        if debug:
            print(f"{indent}lcs({i}, {j}): '{text1[:i]}' vs '{text2[:j]}'")
        
        if (i, j) in memo:
            if debug:
                print(f"{indent}Cache hit: {memo[(i, j)]}")
            return memo[(i, j)]
        
        if i == 0 or j == 0:
            memo[(i, j)] = 0
            return 0
        
        if text1[i-1] == text2[j-1]:
            memo[(i, j)] = 1 + lcs_recursive(i-1, j-1, depth+1)
            if debug:
                print(f"{indent}Match '{text1[i-1]}': 1 + lcs({i-1}, {j-1}) = {memo[(i, j)]}")
        else:
            memo[(i, j)] = max(lcs_recursive(i-1, j, depth+1), lcs_recursive(i, j-1, depth+1))
            if debug:
                print(f"{indent}No match: max(lcs({i-1}, {j}), lcs({i}, {j-1})) = {memo[(i, j)]}")
        
        return memo[(i, j)]
    
    lcs_length = lcs_recursive(len(text1), len(text2))
    
    # Reconstruct LCS string
    lcs_str = ""
    i, j = len(text1), len(text2)
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            lcs_str = text1[i-1] + lcs_str
            i -= 1
            j -= 1
        elif memo.get((i-1, j), 0) > memo.get((i, j-1), 0):
            i -= 1
        else:
            j -= 1
    
    if debug:
        print(f"LCS: '{lcs_str}', Length: {lcs_length}")
    
    return lcs_length, lcs_str


def lcs_tabulation(text1: str, text2: str, debug: bool = False) -> Tuple[int, str]:
    """
    Longest Common Subsequence using tabulation.
    
    Args:
        text1: First string
        text2: Second string
        debug: Enable debug output
    
    Returns:
        Tuple of (lcs_length, lcs_string)
    """
    m, n = len(text1), len(text2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    if debug:
        print(f"LCS tabulation:")
        print(f"Text1: '{text1}'")
        print(f"Text2: '{text2}'")
    
    # Build the LCS table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if debug:
                    print(f"dp[{i}][{j}] = dp[{i-1}][{j-1}] + 1 = {dp[i][j]} (match '{text1[i-1]}')")
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if debug:
                    print(f"dp[{i}][{j}] = max(dp[{i-1}][{j}], dp[{i}][{j-1}]) = {dp[i][j]}")
    
    # Reconstruct LCS
    lcs_str = ""
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            lcs_str = text1[i-1] + lcs_str
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    if debug:
        print(f"DP table:")
        for row in dp:
            print(row)
        print(f"LCS: '{lcs_str}', Length: {dp[m][n]}")
    
    return dp[m][n], lcs_str


# ============================================================================
# LONGEST INCREASING SUBSEQUENCE (LIS)
# ============================================================================

def lis_dp(arr: List[int], debug: bool = False) -> Tuple[int, List[int]]:
    """
    Longest Increasing Subsequence using dynamic programming.
    
    Args:
        arr: Input array
        debug: Enable debug output
    
    Returns:
        Tuple of (lis_length, lis_sequence)
    """
    n = len(arr)
    if n == 0:
        return 0, []
    
    dp = [1] * n  # dp[i] = length of LIS ending at index i
    parent = [-1] * n  # To reconstruct the sequence
    
    if debug:
        print(f"LIS for array: {arr}")
        print(f"Initial dp: {dp}")
    
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
                if debug:
                    print(f"dp[{i}] = dp[{j}] + 1 = {dp[i]} (arr[{j}]={arr[j]} < arr[{i}]={arr[i]})")
    
    # Find the index with maximum LIS length
    max_length = max(dp)
    max_index = dp.index(max_length)
    
    # Reconstruct the LIS
    lis = []
    current = max_index
    while current != -1:
        lis.append(arr[current])
        current = parent[current]
    lis.reverse()
    
    if debug:
        print(f"Final dp: {dp}")
        print(f"LIS length: {max_length}")
        print(f"LIS sequence: {lis}")
    
    return max_length, lis


def lis_binary_search(arr: List[int], debug: bool = False) -> int:
    """
    Longest Increasing Subsequence using binary search (O(n log n)).
    
    Args:
        arr: Input array
        debug: Enable debug output
    
    Returns:
        Length of LIS
    """
    if not arr:
        return 0
    
    tails = []  # tails[i] = smallest ending element of LIS of length i+1
    
    if debug:
        print(f"LIS binary search for array: {arr}")
    
    for num in arr:
        # Binary search for the position to insert/replace
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        # If left == len(tails), extend the sequence
        if left == len(tails):
            tails.append(num)
            if debug:
                print(f"Extended with {num}: {tails}")
        else:
            tails[left] = num
            if debug:
                print(f"Replaced tails[{left}] with {num}: {tails}")
    
    if debug:
        print(f"LIS length: {len(tails)}")
    
    return len(tails)


# ============================================================================
# EDIT DISTANCE (LEVENSHTEIN DISTANCE)
# ============================================================================

def edit_distance(str1: str, str2: str, debug: bool = False) -> Tuple[int, List[str]]:
    """
    Minimum edit distance between two strings.
    
    Args:
        str1: First string
        str2: Second string
        debug: Enable debug output
    
    Returns:
        Tuple of (edit_distance, operations_list)
    """
    m, n = len(str1), len(str2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters from str1
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters to empty string
    
    if debug:
        print(f"Edit distance between '{str1}' and '{str2}':")
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # No operation needed
                if debug:
                    print(f"dp[{i}][{j}] = {dp[i][j]} (match '{str1[i-1]}')")
            else:
                insert = dp[i][j-1] + 1
                delete = dp[i-1][j] + 1
                replace = dp[i-1][j-1] + 1
                dp[i][j] = min(insert, delete, replace)
                if debug:
                    print(f"dp[{i}][{j}] = min(insert={insert}, delete={delete}, replace={replace}) = {dp[i][j]}")
    
    # Backtrack to find operations
    operations = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and str1[i-1] == str2[j-1]:
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + 1:
            operations.append(f"Replace '{str1[i-1]}' with '{str2[j-1]}' at position {i-1}")
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i-1][j] + 1:
            operations.append(f"Delete '{str1[i-1]}' at position {i-1}")
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j-1] + 1:
            operations.append(f"Insert '{str2[j-1]}' at position {i}")
            j -= 1
    
    operations.reverse()
    
    if debug:
        print(f"DP table:")
        for row in dp:
            print(row)
        print(f"Edit distance: {dp[m][n]}")
        print(f"Operations: {operations}")
    
    return dp[m][n], operations


# ============================================================================
# COIN CHANGE PROBLEM
# ============================================================================

def coin_change_dp(coins: List[int], amount: int, debug: bool = False) -> Tuple[int, List[int]]:
    """
    Minimum coins needed to make the given amount.
    
    Args:
        coins: Available coin denominations
        amount: Target amount
        debug: Enable debug output
    
    Returns:
        Tuple of (min_coins, coins_used)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)
    
    if debug:
        print(f"Coin change for amount {amount} with coins {coins}")
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin
                if debug:
                    print(f"dp[{i}] = dp[{i - coin}] + 1 = {dp[i]} (using coin {coin})")
    
    if dp[amount] == float('inf'):
        if debug:
            print("Cannot make the amount with given coins")
        return -1, []
    
    # Reconstruct the solution
    coins_used = []
    current = amount
    while current > 0:
        coin = parent[current]
        coins_used.append(coin)
        current -= coin
    
    if debug:
        print(f"Minimum coins: {dp[amount]}")
        print(f"Coins used: {coins_used}")
    
    return dp[amount], coins_used


def coin_change_ways(coins: List[int], amount: int, debug: bool = False) -> int:
    """
    Number of ways to make the given amount.
    
    Args:
        coins: Available coin denominations
        amount: Target amount
        debug: Enable debug output
    
    Returns:
        Number of ways to make the amount
    """
    dp = [0] * (amount + 1)
    dp[0] = 1  # One way to make amount 0
    
    if debug:
        print(f"Number of ways to make amount {amount} with coins {coins}")
    
    for coin in coins:
        if debug:
            print(f"Processing coin {coin}:")
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
            if debug and dp[i - coin] > 0:
                print(f"  dp[{i}] += dp[{i - coin}] = {dp[i]}")
    
    if debug:
        print(f"Final dp: {dp}")
        print(f"Number of ways: {dp[amount]}")
    
    return dp[amount]


# ============================================================================
# MATRIX CHAIN MULTIPLICATION
# ============================================================================

def matrix_chain_multiplication(dimensions: List[int], debug: bool = False) -> Tuple[int, str]:
    """
    Minimum scalar multiplications for matrix chain multiplication.
    
    Args:
        dimensions: Matrix dimensions [p0, p1, p2, ..., pn] where matrix i has dimensions pi-1 x pi
        debug: Enable debug output
    
    Returns:
        Tuple of (min_operations, optimal_parenthesization)
    """
    n = len(dimensions) - 1  # Number of matrices
    if n < 2:
        return 0, ""
    
    # dp[i][j] = minimum operations to multiply matrices from i to j
    dp = [[0 for _ in range(n)] for _ in range(n)]
    # split[i][j] = optimal split point for matrices i to j
    split = [[0 for _ in range(n)] for _ in range(n)]
    
    if debug:
        print(f"Matrix chain multiplication:")
        print(f"Matrix dimensions: {dimensions}")
        for i in range(n):
            print(f"Matrix {i}: {dimensions[i]} x {dimensions[i+1]}")
    
    # l is chain length
    for length in range(2, n + 1):  # Start from chain length 2
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + dimensions[i] * dimensions[k+1] * dimensions[j+1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k
                    
                if debug:
                    print(f"dp[{i}][{j}] with split at {k}: {dp[i][k]} + {dp[k+1][j]} + {dimensions[i]}*{dimensions[k+1]}*{dimensions[j+1]} = {cost}")
    
    def get_parenthesization(i: int, j: int) -> str:
        if i == j:
            return f"M{i}"
        else:
            k = split[i][j]
            left = get_parenthesization(i, k)
            right = get_parenthesization(k+1, j)
            return f"({left} * {right})"
    
    optimal_parenthesization = get_parenthesization(0, n-1)
    
    if debug:
        print(f"DP table:")
        for row in dp:
            print(row)
        print(f"Minimum operations: {dp[0][n-1]}")
        print(f"Optimal parenthesization: {optimal_parenthesization}")
    
    return dp[0][n-1], optimal_parenthesization


# ============================================================================
# PALINDROME PROBLEMS
# ============================================================================

def longest_palindromic_subsequence(s: str, debug: bool = False) -> Tuple[int, str]:
    """
    Find the longest palindromic subsequence.
    
    Args:
        s: Input string
        debug: Enable debug output
    
    Returns:
        Tuple of (length, palindromic_subsequence)
    """
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    if debug:
        print(f"Longest palindromic subsequence for '{s}':")
    
    # Fill for substrings of length 2 to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i+1][j-1] + 2
                if debug:
                    print(f"dp[{i}][{j}] = {dp[i][j]} (s[{i}]='{s[i]}' == s[{j}]='{s[j]}')")
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                if debug:
                    print(f"dp[{i}][{j}] = max(dp[{i+1}][{j}], dp[{i}][{j-1}]) = {dp[i][j]}")
    
    # Reconstruct the palindromic subsequence
    def reconstruct(i: int, j: int) -> str:
        if i > j:
            return ""
        if i == j:
            return s[i]
        
        if s[i] == s[j]:
            return s[i] + reconstruct(i+1, j-1) + s[j]
        elif dp[i+1][j] > dp[i][j-1]:
            return reconstruct(i+1, j)
        else:
            return reconstruct(i, j-1)
    
    palindrome = reconstruct(0, n-1)
    
    if debug:
        print(f"Length: {dp[0][n-1]}")
        print(f"Palindromic subsequence: '{palindrome}'")
    
    return dp[0][n-1], palindrome


def min_insertions_palindrome(s: str, debug: bool = False) -> Tuple[int, str]:
    """
    Minimum insertions to make string palindrome.
    
    Args:
        s: Input string
        debug: Enable debug output
    
    Returns:
        Tuple of (min_insertions, resulting_palindrome)
    """
    n = len(s)
    lps_length, _ = longest_palindromic_subsequence(s, debug)
    min_insertions = n - lps_length
    
    # To construct the resulting palindrome, we can use LCS between s and reverse(s)
    s_rev = s[::-1]
    _, lcs = lcs_tabulation(s, s_rev, debug=False)
    
    # Construct palindrome by inserting characters
    result = ""
    i = j = 0
    lcs_idx = 0
    
    while i < n or j < n:
        if lcs_idx < len(lcs) and i < n and s[i] == lcs[lcs_idx]:
            result += s[i]
            i += 1
            lcs_idx += 1
        elif lcs_idx < len(lcs) and j < n and s_rev[j] == lcs[lcs_idx]:
            result += s_rev[j]
            j += 1
            lcs_idx += 1
        elif i < n:
            result += s[i]
            i += 1
        elif j < n:
            result += s_rev[j]
            j += 1
    
    if debug:
        print(f"Minimum insertions for '{s}': {min_insertions}")
        print(f"Resulting palindrome: '{result}'")
    
    return min_insertions, result


# ============================================================================
# GRID PATH PROBLEMS
# ============================================================================

def unique_paths(m: int, n: int, debug: bool = False) -> int:
    """
    Number of unique paths in m x n grid from top-left to bottom-right.
    
    Args:
        m: Number of rows
        n: Number of columns
        debug: Enable debug output
    
    Returns:
        Number of unique paths
    """
    dp = [[1 for _ in range(n)] for _ in range(m)]
    
    if debug:
        print(f"Unique paths in {m}x{n} grid:")
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            if debug:
                print(f"dp[{i}][{j}] = dp[{i-1}][{j}] + dp[{i}][{j-1}] = {dp[i-1][j]} + {dp[i][j-1]} = {dp[i][j]}")
    
    if debug:
        print(f"DP table:")
        for row in dp:
            print(row)
        print(f"Total unique paths: {dp[m-1][n-1]}")
    
    return dp[m-1][n-1]


def min_path_sum(grid: List[List[int]], debug: bool = False) -> Tuple[int, List[Tuple[int, int]]]:
    """
    Minimum path sum from top-left to bottom-right in grid.
    
    Args:
        grid: Input grid with costs
        debug: Enable debug output
    
    Returns:
        Tuple of (min_sum, path_coordinates)
    """
    m, n = len(grid), len(grid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    
    # Initialize first cell
    dp[0][0] = grid[0][0]
    
    # Initialize first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Initialize first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    if debug:
        print(f"Minimum path sum in grid:")
        for row in grid:
            print(row)
    
    # Fill the rest of the table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            if debug:
                print(f"dp[{i}][{j}] = min(dp[{i-1}][{j}], dp[{i}][{j-1}]) + grid[{i}][{j}] = min({dp[i-1][j]}, {dp[i][j-1]}) + {grid[i][j]} = {dp[i][j]}")
    
    # Reconstruct path
    path = []
    i, j = m-1, n-1
    while i > 0 or j > 0:
        path.append((i, j))
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        elif dp[i-1][j] < dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    path.append((0, 0))
    path.reverse()
    
    if debug:
        print(f"DP table:")
        for row in dp:
            print(row)
        print(f"Minimum path sum: {dp[m-1][n-1]}")
        print(f"Path: {path}")
    
    return dp[m-1][n-1], path


# ============================================================================
# EXAMPLE USAGE AND TESTING
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("Dynamic Programming Algorithms Demo")
    print("=" * 70)
    
    # 1. Fibonacci Variations
    print("\n1. Fibonacci Variations:")
    n = 10
    print(f"F({n}):")
    print(f"Memoization: {fibonacci_memoization(n, debug=True)}")
    print(f"Tabulation: {fibonacci_tabulation(n, debug=True)}")
    print(f"Space optimized: {fibonacci_space_optimized(n, debug=True)}")
    
    # 2. 0/1 Knapsack
    print("\n2. 0/1 Knapsack Problem:")
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    
    max_val_memo, items_memo = knapsack_01_memoization(weights, values, capacity, debug=True)
    print(f"Memoization: Value = {max_val_memo}, Items = {items_memo}")
    
    max_val_tab, items_tab = knapsack_01_tabulation(weights, values, capacity, debug=True)
    print(f"Tabulation: Value = {max_val_tab}, Items = {items_tab}")
    
    # 3. Longest Common Subsequence
    print("\n3. Longest Common Subsequence:")
    text1, text2 = "ABCDGH", "AEDFHR"
    length_memo, lcs_memo = lcs_memoization(text1, text2, debug=True)
    length_tab, lcs_tab = lcs_tabulation(text1, text2, debug=True)
    
    # 4. Longest Increasing Subsequence
    print("\n4. Longest Increasing Subsequence:")
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    lis_len, lis_seq = lis_dp(arr, debug=True)
    lis_len_fast = lis_binary_search(arr, debug=True)
    
    # 5. Edit Distance
    print("\n5. Edit Distance:")
    str1, str2 = "kitten", "sitting"
    edit_dist, operations = edit_distance(str1, str2, debug=True)
    
    # 6. Coin Change
    print("\n6. Coin Change Problem:")
    coins = [1, 3, 4]
    amount = 6
    min_coins, coins_used = coin_change_dp(coins, amount, debug=True)
    ways = coin_change_ways(coins, amount, debug=True)
    
    # 7. Matrix Chain Multiplication
    print("\n7. Matrix Chain Multiplication:")
    dimensions = [1, 2, 3, 4]  # Matrices: 1x2, 2x3, 3x4
    min_ops, parenthesization = matrix_chain_multiplication(dimensions, debug=True)
    
    # 8. Palindrome Problems
    print("\n8. Palindrome Problems:")
    s = "bbbab"
    lps_len, lps = longest_palindromic_subsequence(s, debug=True)
    min_ins, palindrome = min_insertions_palindrome(s, debug=True)
    
    # 9. Grid Path Problems
    print("\n9. Grid Path Problems:")
    m, n = 3, 3
    paths = unique_paths(m, n, debug=True)
    
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    min_sum, path = min_path_sum(grid, debug=True)
