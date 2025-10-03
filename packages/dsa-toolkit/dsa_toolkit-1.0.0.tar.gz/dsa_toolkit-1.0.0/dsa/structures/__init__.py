"""
Data Structures Package - DSA Toolkit

This package contains implementations of fundamental data structures:

- stack: Stack implementations (ArrayStack, LinkedListStack, MinStack)
- queue: Queue implementations (ArrayQueue, LinkedListQueue, CircularQueue, Deque, PriorityQueue)
- linked_list: Linked list implementations (SinglyLinkedList, DoublyLinkedList, CircularLinkedList)
- tree: Tree implementations (BinaryTree, BinarySearchTree, AVLTree)

Each module includes:
- Multiple implementation approaches
- Debug mode for step-by-step tracing
- Comprehensive examples and test cases
- Type hints and detailed docstrings

Example usage:
    from dsa.structures import stack, queue, linked_list, tree
    
    # Use a stack
    s = stack.ArrayStack()
    s.push(10)
    s.push(20)
    print(s.pop())  # 20
    
    # Use a queue
    q = queue.ArrayQueue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())  # 1
    
    # Use a linked list
    ll = linked_list.SinglyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.display()
    
    # Use a binary search tree
    bst = tree.BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.inorder_traversal()
"""

# Import all modules for easy access
from . import stack
from . import queue
from . import linked_list
from . import tree

__all__ = [
    'stack',
    'queue', 
    'linked_list',
    'tree'
]
