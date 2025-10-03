# DSA Toolkit 🚀

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/dsa-toolkit.svg)](https://badge.fury.io/py/dsa-toolkit)

A comprehensive, educational Python toolkit for **Data Structures and Algorithms (DSA)**. Perfect for students, educators, and developers learning or teaching computer science fundamentals.

## ✨ Features

### 📚 Core Algorithms
- **Sorting**: Bubble, Selection, Insertion, Merge, Quick, Heap, Counting, Radix, Shell Sort
- **Searching**: Linear, Binary (iterative & recursive), Jump, Exponential, Interpolation
- **Recursion**: Factorial, Fibonacci, Power, GCD, Tower of Hanoi, and more
- **Graph Algorithms**: DFS, BFS, Dijkstra, and more

### 🏗️ Data Structures
- **Stacks**: Array-based, Linked List-based, Min Stack
- **Queues**: Array Queue, Linked List Queue, Circular Queue, Deque, Priority Queue
- **Linked Lists**: Singly, Doubly, Circular
- **Trees**: Binary Tree, Binary Search Tree (BST), AVL Tree

### 🎯 Advanced Algorithms
- **Greedy**: Activity Selection, Fractional Knapsack, Huffman Coding, Job Scheduling
- **Divide & Conquer**: Advanced sorting, Closest Pair, Strassen's Matrix Multiplication
- **Dynamic Programming**: 0/1 Knapsack, LCS, LIS, Edit Distance, Coin Change, Matrix Chain Multiplication

## 🔧 Installation

### From PyPI (Recommended)
```bash
pip install dsa-toolkit
```

### From Source
```bash
git clone https://github.com/masoomverma/dsa-toolkit.git
cd dsa-toolkit
pip install -e .
```

## 🚀 Quick Start

```python
# Import modules
from dsa import sorting, searching, recursion
from dsa.structures import stack, queue, tree
from dsa.algorithms import greedy, dynamic_programming

# Use sorting algorithms with debug mode
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = sorting.quick_sort(arr, debug=True)

# Work with data structures
s = stack.ArrayStack(debug=True)
s.push(10)
s.push(20)
print(s.pop())  # 20

# Use advanced algorithms
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value, items = greedy.fractional_knapsack(
    list(zip(values, weights)), 
    capacity, 
    debug=True
)
```

## 📖 Usage Examples

### Sorting with Debug Mode
```python
from dsa import sorting

arr = [5, 2, 8, 1, 9]
result = sorting.merge_sort(arr, debug=True)
# Outputs step-by-step execution trace
```

### Binary Search Tree
```python
from dsa.structures import tree

bst = tree.BinarySearchTree(debug=True)
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(val)

print(bst.inorder_traversal())  # [20, 30, 40, 50, 60, 70, 80]
print(bst.search(40))  # True
```

### Dynamic Programming
```python
from dsa.algorithms import dynamic_programming

# 0/1 Knapsack Problem
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

max_value, selected_items = dynamic_programming.knapsack_01_tabulation(
    weights, values, capacity, debug=True
)
print(f"Maximum value: {max_value}")
```

### Stack Applications
```python
from dsa.structures.stack import is_balanced_parentheses, evaluate_postfix

# Check balanced parentheses
expression = "([{}])"
is_balanced = is_balanced_parentheses(expression, debug=True)

# Evaluate postfix expression
postfix = "3 4 + 2 * 7 /"
result = evaluate_postfix(postfix, debug=True)
```

## 🎓 Educational Features

### Debug Mode
Every algorithm and data structure supports a `debug=True` parameter that provides:
- Step-by-step execution traces
- Intermediate states and values
- Decision-making processes
- Visual representation of operations

```python
from dsa import sorting

# See exactly how bubble sort works
arr = [5, 1, 4, 2, 8]
sorting.bubble_sort(arr, debug=True)
```

### Comprehensive Documentation
- Detailed docstrings for all functions and classes
- Time and space complexity information
- Real-world use cases and examples

## 📦 Package Structure

```
dsa/
├── __init__.py
├── sorting.py              # Sorting algorithms
├── searching.py            # Searching algorithms
├── recursion.py            # Recursive algorithms
├── graph.py                # Graph algorithms
├── utils.py                # Utility functions
├── structures/
│   ├── __init__.py
│   ├── stack.py            # Stack implementations
│   ├── queue.py            # Queue implementations
│   ├── linked_list.py      # Linked list implementations
│   └── tree.py             # Tree implementations
└── algorithms/
    ├── __init__.py
    ├── greedy.py           # Greedy algorithms
    ├── divide_and_conquer.py
    └── dynamic_programming.py
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built for educational purposes
- Inspired by classic computer science textbooks
- Designed to help students and developers master DSA concepts

## 📧 Contact

Masoom Verma - 0xmasoom@gmail.com

Project Link: [https://github.com/masoomverma/dsa-toolkit](https://github.com/masoomverma/dsa-toolkit)

## 🌟 Star History

If you find this project helpful, please consider giving it a star ⭐!

---

**Happy Learning! 📚✨**
