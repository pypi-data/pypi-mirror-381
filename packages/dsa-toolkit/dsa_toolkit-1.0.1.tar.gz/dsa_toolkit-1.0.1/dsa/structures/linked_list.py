"""
linked_list.py - DSA Toolkit

This module implements various Linked List data structures:
- Singly Linked List
- Doubly Linked List
- Circular Linked List
- Common operations and algorithms

Features:
- Insert, delete, search operations
- Optional debug tracing
- List traversal and manipulation
- Advanced algorithms (reverse, merge, etc.)
"""

from typing import Any, Optional, List


# ============================================================================
# SINGLY LINKED LIST
# ============================================================================

class SinglyListNode:
    """Node for singly linked list."""
    
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['SinglyListNode'] = None
    
    def __str__(self) -> str:
        return str(self.data)


class SinglyLinkedList:
    """Singly Linked List implementation."""
    
    def __init__(self, debug: bool = False):
        """Initialize an empty linked list."""
        self.head: Optional[SinglyListNode] = None
        self._size = 0
        self._debug = debug
        if self._debug:
            print("SinglyLinkedList initialized")
    
    def insert_at_beginning(self, data: Any) -> None:
        """Insert a new node at the beginning of the list."""
        new_node = SinglyListNode(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
        if self._debug:
            print(f"Inserted {data} at beginning. Size: {self._size}")
    
    def insert_at_end(self, data: Any) -> None:
        """Insert a new node at the end of the list."""
        new_node = SinglyListNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1
        if self._debug:
            print(f"Inserted {data} at end. Size: {self._size}")
    
    def insert_at_position(self, data: Any, position: int) -> None:
        """Insert a new node at the specified position."""
        if position < 0 or position > self._size:
            raise IndexError(f"Position {position} out of range")
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = SinglyListNode(data)
        current = self.head
        for _ in range(position - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self._size += 1
        if self._debug:
            print(f"Inserted {data} at position {position}. Size: {self._size}")
    
    def delete_at_beginning(self) -> Any:
        """Delete the first node and return its data."""
        if not self.head:
            raise IndexError("Delete from empty list")
        
        data = self.head.data
        self.head = self.head.next
        self._size -= 1
        if self._debug:
            print(f"Deleted {data} from beginning. Size: {self._size}")
        return data
    
    def delete_at_end(self) -> Any:
        """Delete the last node and return its data."""
        if not self.head:
            raise IndexError("Delete from empty list")
        
        if not self.head.next:  # Only one node
            data = self.head.data
            self.head = None
            self._size -= 1
            if self._debug:
                print(f"Deleted {data} from end. Size: {self._size}")
            return data
        
        current = self.head
        while current.next.next:
            current = current.next
        
        data = current.next.data
        current.next = None
        self._size -= 1
        if self._debug:
            print(f"Deleted {data} from end. Size: {self._size}")
        return data
    
    def delete_by_value(self, value: Any) -> bool:
        """Delete the first node with the specified value."""
        if not self.head:
            return False
        
        if self.head.data == value:
            self.delete_at_beginning()
            return True
        
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                self._size -= 1
                if self._debug:
                    print(f"Deleted {value}. Size: {self._size}")
                return True
            current = current.next
        
        return False
    
    def search(self, value: Any) -> int:
        """Search for a value and return its position (-1 if not found)."""
        current = self.head
        position = 0
        
        while current:
            if self._debug:
                print(f"Searching: position {position}, value {current.data}")
            if current.data == value:
                if self._debug:
                    print(f"Found {value} at position {position}")
                return position
            current = current.next
            position += 1
        
        if self._debug:
            print(f"{value} not found")
        return -1
    
    def reverse(self) -> None:
        """Reverse the linked list."""
        prev = None
        current = self.head
        
        while current:
            if self._debug:
                print(f"Reversing: current={current.data}")
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
        if self._debug:
            print("List reversed")
    
    def get_middle(self) -> Any:
        """Get the middle element using Floyd's algorithm."""
        if not self.head:
            raise IndexError("Empty list")
        
        slow = fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        if self._debug:
            print(f"Middle element: {slow.data}")
        return slow.data
    
    def detect_cycle(self) -> bool:
        """Detect if there's a cycle in the list using Floyd's algorithm."""
        if not self.head:
            return False
        
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                if self._debug:
                    print("Cycle detected")
                return True
        
        if self._debug:
            print("No cycle detected")
        return False
    
    def size(self) -> int:
        """Return the size of the list."""
        return self._size
    
    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self.head is None
    
    def to_list(self) -> List[Any]:
        """Convert linked list to Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def __str__(self) -> str:
        """String representation of the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) + " -> None"


# ============================================================================
# DOUBLY LINKED LIST
# ============================================================================

class DoublyListNode:
    """Node for doubly linked list."""
    
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['DoublyListNode'] = None
        self.prev: Optional['DoublyListNode'] = None
    
    def __str__(self) -> str:
        return str(self.data)


class DoublyLinkedList:
    """Doubly Linked List implementation."""
    
    def __init__(self, debug: bool = False):
        """Initialize an empty doubly linked list."""
        self.head: Optional[DoublyListNode] = None
        self.tail: Optional[DoublyListNode] = None
        self._size = 0
        self._debug = debug
        if self._debug:
            print("DoublyLinkedList initialized")
    
    def insert_at_beginning(self, data: Any) -> None:
        """Insert a new node at the beginning."""
        new_node = DoublyListNode(data)
        
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self._size += 1
        if self._debug:
            print(f"Inserted {data} at beginning. Size: {self._size}")
    
    def insert_at_end(self, data: Any) -> None:
        """Insert a new node at the end."""
        new_node = DoublyListNode(data)
        
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self._size += 1
        if self._debug:
            print(f"Inserted {data} at end. Size: {self._size}")
    
    def delete_at_beginning(self) -> Any:
        """Delete the first node and return its data."""
        if not self.head:
            raise IndexError("Delete from empty list")
        
        data = self.head.data
        
        if self.head == self.tail:  # Only one node
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        
        self._size -= 1
        if self._debug:
            print(f"Deleted {data} from beginning. Size: {self._size}")
        return data
    
    def delete_at_end(self) -> Any:
        """Delete the last node and return its data."""
        if not self.tail:
            raise IndexError("Delete from empty list")
        
        data = self.tail.data
        
        if self.head == self.tail:  # Only one node
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        self._size -= 1
        if self._debug:
            print(f"Deleted {data} from end. Size: {self._size}")
        return data
    
    def traverse_forward(self) -> List[Any]:
        """Traverse the list from head to tail."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def traverse_backward(self) -> List[Any]:
        """Traverse the list from tail to head."""
        result = []
        current = self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result
    
    def size(self) -> int:
        """Return the size of the list."""
        return self._size
    
    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self.head is None
    
    def __str__(self) -> str:
        """String representation of the doubly linked list."""
        forward = self.traverse_forward()
        return "None <- " + " <-> ".join(map(str, forward)) + " -> None"


# ============================================================================
# CIRCULAR LINKED LIST
# ============================================================================

class CircularLinkedList:
    """Circular Linked List implementation."""
    
    def __init__(self, debug: bool = False):
        """Initialize an empty circular linked list."""
        self.head: Optional[SinglyListNode] = None
        self._size = 0
        self._debug = debug
        if self._debug:
            print("CircularLinkedList initialized")
    
    def insert_at_beginning(self, data: Any) -> None:
        """Insert a new node at the beginning."""
        new_node = SinglyListNode(data)
        
        if not self.head:
            self.head = new_node
            new_node.next = new_node  # Points to itself
        else:
            # Find the last node
            current = self.head
            while current.next != self.head:
                current = current.next
            
            new_node.next = self.head
            current.next = new_node
            self.head = new_node
        
        self._size += 1
        if self._debug:
            print(f"Inserted {data} at beginning. Size: {self._size}")
    
    def insert_at_end(self, data: Any) -> None:
        """Insert a new node at the end."""
        new_node = SinglyListNode(data)
        
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            
            current.next = new_node
            new_node.next = self.head
        
        self._size += 1
        if self._debug:
            print(f"Inserted {data} at end. Size: {self._size}")
    
    def delete_by_value(self, value: Any) -> bool:
        """Delete the first node with the specified value."""
        if not self.head:
            return False
        
        current = self.head
        prev = None
        
        # Find the node to delete
        while True:
            if current.data == value:
                break
            prev = current
            current = current.next
            if current == self.head:  # Completed full circle
                return False
        
        # If it's the only node
        if current.next == current:
            self.head = None
        else:
            # Find the last node
            last = self.head
            while last.next != self.head:
                last = last.next
            
            if current == self.head:  # Deleting head
                self.head = current.next
                last.next = self.head
            else:
                prev.next = current.next
        
        self._size -= 1
        if self._debug:
            print(f"Deleted {value}. Size: {self._size}")
        return True
    
    def traverse(self, max_iterations: int = None) -> List[Any]:
        """Traverse the circular list (with optional max iterations)."""
        if not self.head:
            return []
        
        result = []
        current = self.head
        iterations = 0
        max_iter = max_iterations or self._size
        
        while iterations < max_iter:
            result.append(current.data)
            current = current.next
            iterations += 1
            if current == self.head and iterations >= self._size:
                break
        
        return result
    
    def size(self) -> int:
        """Return the size of the list."""
        return self._size
    
    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self.head is None
    
    def __str__(self) -> str:
        """String representation of the circular linked list."""
        elements = self.traverse()
        if not elements:
            return "Empty circular list"
        return " -> ".join(map(str, elements)) + f" -> {elements[0]} (circular)"


# ============================================================================
# LINKED LIST ALGORITHMS
# ============================================================================

def merge_sorted_lists(list1: SinglyLinkedList, list2: SinglyLinkedList, debug: bool = False) -> SinglyLinkedList:
    """Merge two sorted linked lists into one sorted list."""
    merged = SinglyLinkedList(debug=debug)
    current1 = list1.head
    current2 = list2.head
    
    while current1 and current2:
        if current1.data <= current2.data:
            merged.insert_at_end(current1.data)
            current1 = current1.next
        else:
            merged.insert_at_end(current2.data)
            current2 = current2.next
    
    # Add remaining elements
    while current1:
        merged.insert_at_end(current1.data)
        current1 = current1.next
    
    while current2:
        merged.insert_at_end(current2.data)
        current2 = current2.next
    
    return merged


def find_intersection(list1: SinglyLinkedList, list2: SinglyLinkedList, debug: bool = False) -> Optional[Any]:
    """Find the intersection point of two linked lists."""
    if not list1.head or not list2.head:
        return None
    
    # Get lengths
    len1 = list1.size()
    len2 = list2.size()
    
    current1 = list1.head
    current2 = list2.head
    
    # Align the starting points
    if len1 > len2:
        for _ in range(len1 - len2):
            current1 = current1.next
    else:
        for _ in range(len2 - len1):
            current2 = current2.next
    
    # Find intersection
    while current1 and current2:
        if current1 == current2:
            if debug:
                print(f"Intersection found at node with data: {current1.data}")
            return current1.data
        current1 = current1.next
        current2 = current2.next
    
    if debug:
        print("No intersection found")
    return None


def remove_duplicates(linked_list: SinglyLinkedList, debug: bool = False) -> None:
    """Remove duplicates from a sorted linked list."""
    current = linked_list.head
    
    while current and current.next:
        if current.data == current.next.data:
            if debug:
                print(f"Removing duplicate: {current.next.data}")
            current.next = current.next.next
            linked_list._size -= 1
        else:
            current = current.next


# ============================================================================
# EXAMPLE USAGE AND TESTING
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Linked List Data Structures Demo")
    print("=" * 60)
    
    # 1. Singly Linked List Demo
    print("\n1. Singly Linked List Demo:")
    sll = SinglyLinkedList(debug=True)
    
    # Insert operations
    sll.insert_at_beginning(10)
    sll.insert_at_end(20)
    sll.insert_at_end(30)
    sll.insert_at_position(15, 1)
    
    print(f"List: {sll}")
    print(f"Size: {sll.size()}")
    
    # Search operations
    print(f"Search 20: position {sll.search(20)}")
    print(f"Search 99: position {sll.search(99)}")
    
    # Middle element
    print(f"Middle element: {sll.get_middle()}")
    
    # Reverse the list
    sll.reverse()
    print(f"Reversed list: {sll}")
    
    # 2. Doubly Linked List Demo
    print("\n2. Doubly Linked List Demo:")
    dll = DoublyLinkedList(debug=True)
    
    for i in [1, 2, 3, 4, 5]:
        dll.insert_at_end(i)
    
    print(f"Forward traversal: {dll.traverse_forward()}")
    print(f"Backward traversal: {dll.traverse_backward()}")
    print(f"List: {dll}")
    
    # 3. Circular Linked List Demo
    print("\n3. Circular Linked List Demo:")
    cll = CircularLinkedList(debug=True)
    
    for i in ['A', 'B', 'C']:
        cll.insert_at_end(i)
    
    print(f"Circular list: {cll}")
    print(f"Traversal (2 rounds): {cll.traverse(6)}")
    
    # 4. Merge Sorted Lists Demo
    print("\n4. Merge Sorted Lists Demo:")
    list1 = SinglyLinkedList()
    list2 = SinglyLinkedList()
    
    for i in [1, 3, 5]:
        list1.insert_at_end(i)
    for i in [2, 4, 6]:
        list2.insert_at_end(i)
    
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    
    merged = merge_sorted_lists(list1, list2, debug=True)
    print(f"Merged: {merged}")
    
    # 5. Remove Duplicates Demo
    print("\n5. Remove Duplicates Demo:")
    dup_list = SinglyLinkedList(debug=True)
    for i in [1, 1, 2, 3, 3, 3, 4]:
        dup_list.insert_at_end(i)
    
    print(f"List with duplicates: {dup_list}")
    remove_duplicates(dup_list, debug=True)
    print(f"After removing duplicates: {dup_list}")
    
    # 6. Cycle Detection Demo
    print("\n6. Cycle Detection Demo:")
    cycle_list = SinglyLinkedList(debug=True)
    for i in [1, 2, 3, 4]:
        cycle_list.insert_at_end(i)
    
    print(f"List without cycle: {cycle_list}")
    print(f"Cycle detected: {cycle_list.detect_cycle()}")
    
    # Create a cycle (for demonstration - normally avoid this)
    # cycle_list.head.next.next.next.next = cycle_list.head.next
    # print(f"After creating cycle, cycle detected: {cycle_list.detect_cycle()}")
