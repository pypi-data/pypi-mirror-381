"""
stack.py - DSA Toolkit

This module implements Stack data structure using different approaches:
- Stack using Python List (Array-based)
- Stack using Linked List
- Stack with additional operations (peek, size, is_empty)

Features:
- Push and Pop operations
- Optional debug tracing
- Multiple implementations
- Comprehensive examples
"""

from typing import Any, Optional


# ============================================================================
# STACK USING PYTHON LIST (ARRAY-BASED)
# ============================================================================

class ArrayStack:
    """Stack implementation using Python list (dynamic array)."""
    
    def __init__(self, debug: bool = False):
        """Initialize an empty stack."""
        self._items = []
        self._debug = debug
        if self._debug:
            print("ArrayStack initialized")
    
    def push(self, item: Any) -> None:
        """Add an item to the top of the stack."""
        self._items.append(item)
        if self._debug:
            print(f"Pushed {item} to stack. Size: {len(self._items)}")
    
    def pop(self) -> Any:
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        item = self._items.pop()
        if self._debug:
            print(f"Popped {item} from stack. Size: {len(self._items)}")
        return item
    
    def peek(self) -> Any:
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        item = self._items[-1]
        if self._debug:
            print(f"Peeked {item} from stack")
        return item
    
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)
    
    def clear(self) -> None:
        """Remove all items from the stack."""
        self._items.clear()
        if self._debug:
            print("Stack cleared")
    
    def to_list(self) -> list:
        """Return stack contents as a list (top to bottom)."""
        return self._items[::-1]
    
    def __str__(self) -> str:
        """String representation of the stack."""
        return f"ArrayStack({self._items})"
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        return self.__str__()


# ============================================================================
# STACK USING LINKED LIST
# ============================================================================

class ListNode:
    """Node for linked list implementation."""
    
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['ListNode'] = None


class LinkedListStack:
    """Stack implementation using linked list."""
    
    def __init__(self, debug: bool = False):
        """Initialize an empty stack."""
        self._top: Optional[ListNode] = None
        self._size = 0
        self._debug = debug
        if self._debug:
            print("LinkedListStack initialized")
    
    def push(self, item: Any) -> None:
        """Add an item to the top of the stack."""
        new_node = ListNode(item)
        new_node.next = self._top
        self._top = new_node
        self._size += 1
        if self._debug:
            print(f"Pushed {item} to stack. Size: {self._size}")
    
    def pop(self) -> Any:
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        item = self._top.data
        self._top = self._top.next
        self._size -= 1
        if self._debug:
            print(f"Popped {item} from stack. Size: {self._size}")
        return item
    
    def peek(self) -> Any:
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        item = self._top.data
        if self._debug:
            print(f"Peeked {item} from stack")
        return item
    
    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return self._top is None
    
    def size(self) -> int:
        """Return the number of items in the stack."""
        return self._size
    
    def clear(self) -> None:
        """Remove all items from the stack."""
        self._top = None
        self._size = 0
        if self._debug:
            print("Stack cleared")
    
    def to_list(self) -> list:
        """Return stack contents as a list (top to bottom)."""
        result = []
        current = self._top
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def __str__(self) -> str:
        """String representation of the stack."""
        return f"LinkedListStack({self.to_list()})"
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        return self.__str__()


# ============================================================================
# STACK WITH MIN OPERATION (OPTIMIZATION PROBLEM)
# ============================================================================

class MinStack:
    """Stack that supports getting minimum element in O(1) time."""
    
    def __init__(self, debug: bool = False):
        """Initialize stack with min tracking."""
        self._stack = []
        self._min_stack = []
        self._debug = debug
        if self._debug:
            print("MinStack initialized")
    
    def push(self, item: Any) -> None:
        """Push item to stack while maintaining min tracking."""
        self._stack.append(item)
        if not self._min_stack or item <= self._min_stack[-1]:
            self._min_stack.append(item)
        if self._debug:
            print(f"Pushed {item}. Current min: {self.get_min() if self._min_stack else 'None'}")
    
    def pop(self) -> Any:
        """Pop item from stack while maintaining min tracking."""
        if not self._stack:
            raise IndexError("Pop from empty stack")
        item = self._stack.pop()
        if self._min_stack and item == self._min_stack[-1]:
            self._min_stack.pop()
        if self._debug:
            print(f"Popped {item}. Current min: {self.get_min() if self._min_stack else 'None'}")
        return item
    
    def peek(self) -> Any:
        """Get top item without removing it."""
        if not self._stack:
            raise IndexError("Peek from empty stack")
        return self._stack[-1]
    
    def get_min(self) -> Any:
        """Get minimum element in O(1) time."""
        if not self._min_stack:
            raise IndexError("No minimum in empty stack")
        return self._min_stack[-1]
    
    def is_empty(self) -> bool:
        """Check if stack is empty."""
        return len(self._stack) == 0
    
    def size(self) -> int:
        """Get size of stack."""
        return len(self._stack)


# ============================================================================
# STACK APPLICATIONS
# ============================================================================

def is_balanced_parentheses(expression: str, debug: bool = False) -> bool:
    """Check if parentheses are balanced using stack."""
    stack = ArrayStack(debug=debug)
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in pairs:  # Opening bracket
            stack.push(char)
            if debug:
                print(f"Found opening bracket: {char}")
        elif char in pairs.values():  # Closing bracket
            if stack.is_empty():
                if debug:
                    print(f"Found closing bracket {char} with no matching opening")
                return False
            opening = stack.pop()
            if pairs[opening] != char:
                if debug:
                    print(f"Mismatched: {opening} and {char}")
                return False
            if debug:
                print(f"Matched: {opening} and {char}")
    
    result = stack.is_empty()
    if debug:
        print(f"Final result: {'Balanced' if result else 'Not balanced'}")
    return result


def evaluate_postfix(expression: str, debug: bool = False) -> float:
    """Evaluate postfix expression using stack."""
    stack = ArrayStack(debug=debug)
    tokens = expression.split()
    
    for token in tokens:
        if debug:
            print(f"Processing token: {token}")
        
        if token in ['+', '-', '*', '/']:
            if stack.size() < 2:
                raise ValueError("Invalid postfix expression")
            
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                if b == 0:
                    raise ValueError("Division by zero")
                result = a / b
            
            stack.push(result)
            if debug:
                print(f"Calculated {a} {token} {b} = {result}")
        else:
            try:
                number = float(token)
                stack.push(number)
                if debug:
                    print(f"Pushed number: {number}")
            except ValueError:
                raise ValueError(f"Invalid token: {token}")
    
    if stack.size() != 1:
        raise ValueError("Invalid postfix expression")
    
    return stack.pop()


def infix_to_postfix(expression: str, debug: bool = False) -> str:
    """Convert infix expression to postfix using stack."""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = ArrayStack(debug=debug)
    result = []
    
    for char in expression:
        if debug:
            print(f"Processing: {char}")
        
        if char.isalnum():  # Operand
            result.append(char)
            if debug:
                print(f"Added operand to result: {char}")
        elif char == '(':
            stack.push(char)
            if debug:
                print("Pushed opening parenthesis")
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                op = stack.pop()
                result.append(op)
                if debug:
                    print(f"Popped operator: {op}")
            stack.pop()  # Remove '('
            if debug:
                print("Removed opening parenthesis")
        elif char in precedence:
            while (not stack.is_empty() and 
                   stack.peek() != '(' and 
                   stack.peek() in precedence and
                   precedence[stack.peek()] >= precedence[char]):
                op = stack.pop()
                result.append(op)
                if debug:
                    print(f"Popped higher precedence operator: {op}")
            stack.push(char)
            if debug:
                print(f"Pushed operator: {char}")
    
    while not stack.is_empty():
        op = stack.pop()
        result.append(op)
        if debug:
            print(f"Popped remaining operator: {op}")
    
    return ' '.join(result)


# ============================================================================
# EXAMPLE USAGE AND TESTING
# ============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("Stack Data Structure Demo")
    print("=" * 50)
    
    # 1. Array Stack Demo
    print("\n1. Array Stack Demo:")
    array_stack = ArrayStack(debug=True)
    for i in [10, 20, 30]:
        array_stack.push(i)
    
    print(f"Stack contents: {array_stack.to_list()}")
    print(f"Peek: {array_stack.peek()}")
    print(f"Pop: {array_stack.pop()}")
    print(f"Size: {array_stack.size()}")
    
    # 2. Linked List Stack Demo
    print("\n2. Linked List Stack Demo:")
    ll_stack = LinkedListStack(debug=True)
    for i in ['A', 'B', 'C']:
        ll_stack.push(i)
    
    print(f"Stack contents: {ll_stack.to_list()}")
    print(f"Pop: {ll_stack.pop()}")
    print(f"Size: {ll_stack.size()}")
    
    # 3. Min Stack Demo
    print("\n3. Min Stack Demo:")
    min_stack = MinStack(debug=True)
    for num in [5, 2, 8, 1, 3]:
        min_stack.push(num)
        print(f"Current minimum: {min_stack.get_min()}")
    
    # 4. Balanced Parentheses Demo
    print("\n4. Balanced Parentheses Demo:")
    test_expressions = [
        "((()))",
        "([{}])",
        "(((",
        "()[]{}",
        "([)]"
    ]
    
    for expr in test_expressions:
        result = is_balanced_parentheses(expr, debug=True)
        print(f"'{expr}' is {'balanced' if result else 'not balanced'}\n")
    
    # 5. Postfix Evaluation Demo
    print("\n5. Postfix Evaluation Demo:")
    postfix_expr = "3 4 + 2 * 7 /"
    result = evaluate_postfix(postfix_expr, debug=True)
    print(f"Result of '{postfix_expr}': {result}")
    
    # 6. Infix to Postfix Demo
    print("\n6. Infix to Postfix Demo:")
    infix_expr = "A+B*C"
    postfix_result = infix_to_postfix(infix_expr, debug=True)
    print(f"Infix: {infix_expr}")
    print(f"Postfix: {postfix_result}")
