"""
recursion.py - DSA Toolkit

This module implements classic recursive algorithms with optional debug tracing:
- Factorial (Recursive, Tail Recursive)
- Fibonacci (Naive, Memoized, Bottom-Up)
- Power (Fast Exponentiation)
- Sum of Digits
- GCD (Euclidean)
- Reverse String & Number
- Tower of Hanoi
- Count Stair Ways
"""

def factorial(n, debug=False):
    if debug: print(f"factorial({n})")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1, debug)

def factorial_tail(n, acc=1, debug=False):
    if debug: print(f"factorial_tail({n}, {acc})")
    if n == 0:
        return acc
    return factorial_tail(n - 1, acc * n, debug)

def fibonacci(n, debug=False):
    if debug: print(f"fibonacci({n})")
    if n <= 1:
        return n
    return fibonacci(n - 1, debug) + fibonacci(n - 2, debug)

def fibonacci_memo(n, memo=None, debug=False):
    if memo is None:
        memo = {}
    if debug: print(f"fibonacci_memo({n})")
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo, debug) + fibonacci_memo(n-2, memo, debug)
    return memo[n]

def fibonacci_bottom_up(n, debug=False):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a + b
        if debug: print(f"i: {i}, value: {b}")
    return b

def power(a, b, debug=False):
    if debug: print(f"power({a}, {b})")
    if b == 0:
        return 1
    half = power(a, b // 2, debug)
    if b % 2 == 0:
        return half * half
    return half * half * a

def sum_of_digits(n, debug=False):
    if debug: print(f"sum_of_digits({n})")
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10, debug)

def gcd(a, b, debug=False):
    if debug: print(f"gcd({a}, {b})")
    if b == 0:
        return a
    return gcd(b, a % b, debug)

def reverse_string(s, debug=False):
    if debug: print(f"reverse_string('{s}')")
    if len(s) == 0:
        return ""
    return reverse_string(s[1:], debug) + s[0]

def reverse_number(n, result=0, debug=False):
    if debug: print(f"reverse_number({n}, {result})")
    if n == 0:
        return result
    return reverse_number(n // 10, result * 10 + n % 10, debug)

def tower_of_hanoi(n, source, target, auxiliary, steps=None, debug=False):
    if steps is None:
        steps = []
    if n == 1:
        move = f"Move disk 1 from {source} to {target}"
        if debug: print(move)
        steps.append(move)
        return steps
    tower_of_hanoi(n-1, source, auxiliary, target, steps, debug)
    move = f"Move disk {n} from {source} to {target}"
    if debug: print(move)
    steps.append(move)
    tower_of_hanoi(n-1, auxiliary, target, source, steps, debug)
    return steps

def count_stair_ways(n, debug=False):
    if debug: print(f"count_stair_ways({n})")
    if n <= 1:
        return 1
    return count_stair_ways(n-1, debug) + count_stair_ways(n-2, debug)

# Sample usage
if __name__ == "__main__":
    print("Factorial (5):", factorial(5, debug=True))
    print("Fibonacci (5):", fibonacci(5, debug=True))
    print("Fibonacci Memo (7):", fibonacci_memo(7, debug=True))
    print("Fibonacci Bottom Up (7):", fibonacci_bottom_up(7, debug=True))
    print("Power (2^5):", power(2, 5, debug=True))
    print("Sum of Digits (1234):", sum_of_digits(1234, debug=True))
    print("GCD (48, 18):", gcd(48, 18, debug=True))
    print("Reverse String ('hello'):", reverse_string("hello", debug=True))
    print("Reverse Number (1234):", reverse_number(1234, debug=True))
    print("Tower of Hanoi (3 disks):")
    for step in tower_of_hanoi(3, 'A', 'C', 'B', debug=True):
        print(step)
    print("Ways to reach 5 stairs:", count_stair_ways(5, debug=True))
