"""
queue.py - DSA Toolkit

This module implements various Queue data structures:
- Basic Queue using Python List
- Queue using Linked List
- Circular Queue
- Double-ended Queue (Deque)
- Priority Queue

Features:
- Enqueue and Dequeue operations
- Optional debug tracing
- Multiple implementations
- Queue applications and examples
"""

from typing import Any, Optional
import heapq
from collections import deque


# ============================================================================
# BASIC QUEUE USING PYTHON LIST
# ============================================================================

class ArrayQueue:
    """Queue implementation using Python list (not efficient for large queues)."""
    
    def __init__(self, debug: bool = False):
        """Initialize an empty queue."""
        self._items = []
        self._debug = debug
        if self._debug:
            print("ArrayQueue initialized")
    
    def enqueue(self, item: Any) -> None:
        """Add an item to the rear of the queue."""
        self._items.append(item)
        if self._debug:
            print(f"Enqueued {item}. Queue size: {len(self._items)}")
    
    def dequeue(self) -> Any:
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        item = self._items.pop(0)  # O(n) operation!
        if self._debug:
            print(f"Dequeued {item}. Queue size: {len(self._items)}")
        return item
    
    def front(self) -> Any:
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Front of empty queue")
        return self._items[0]
    
    def rear(self) -> Any:
        """Return the rear item without removing it."""
        if self.is_empty():
            raise IndexError("Rear of empty queue")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Return the number of items in the queue."""
        return len(self._items)
    
    def clear(self) -> None:
        """Remove all items from the queue."""
        self._items.clear()
        if self._debug:
            print("Queue cleared")
    
    def to_list(self) -> list:
        """Return queue contents as a list (front to rear)."""
        return self._items.copy()
    
    def __str__(self) -> str:
        """String representation of the queue."""
        return f"ArrayQueue(front -> {self._items} <- rear)"


# ============================================================================
# QUEUE USING LINKED LIST (EFFICIENT)
# ============================================================================

class QueueNode:
    """Node for linked list queue implementation."""
    
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['QueueNode'] = None


class LinkedListQueue:
    """Efficient queue implementation using linked list."""
    
    def __init__(self, debug: bool = False):
        """Initialize an empty queue."""
        self._front: Optional[QueueNode] = None
        self._rear: Optional[QueueNode] = None
        self._size = 0
        self._debug = debug
        if self._debug:
            print("LinkedListQueue initialized")
    
    def enqueue(self, item: Any) -> None:
        """Add an item to the rear of the queue."""
        new_node = QueueNode(item)
        if self._rear is None:  # Empty queue
            self._front = self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        self._size += 1
        if self._debug:
            print(f"Enqueued {item}. Queue size: {self._size}")
    
    def dequeue(self) -> Any:
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        
        item = self._front.data
        self._front = self._front.next
        if self._front is None:  # Queue became empty
            self._rear = None
        self._size -= 1
        if self._debug:
            print(f"Dequeued {item}. Queue size: {self._size}")
        return item
    
    def front(self) -> Any:
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Front of empty queue")
        return self._front.data
    
    def rear(self) -> Any:
        """Return the rear item without removing it."""
        if self.is_empty():
            raise IndexError("Rear of empty queue")
        return self._rear.data
    
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return self._front is None
    
    def size(self) -> int:
        """Return the number of items in the queue."""
        return self._size
    
    def clear(self) -> None:
        """Remove all items from the queue."""
        self._front = self._rear = None
        self._size = 0
        if self._debug:
            print("Queue cleared")
    
    def to_list(self) -> list:
        """Return queue contents as a list (front to rear)."""
        result = []
        current = self._front
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def __str__(self) -> str:
        """String representation of the queue."""
        return f"LinkedListQueue(front -> {self.to_list()} <- rear)"


# ============================================================================
# CIRCULAR QUEUE (FIXED SIZE)
# ============================================================================

class CircularQueue:
    """Circular queue implementation with fixed capacity."""
    
    def __init__(self, capacity: int, debug: bool = False):
        """Initialize circular queue with given capacity."""
        self._capacity = capacity
        self._items = [None] * capacity
        self._front = -1
        self._rear = -1
        self._size = 0
        self._debug = debug
        if self._debug:
            print(f"CircularQueue initialized with capacity {capacity}")
    
    def enqueue(self, item: Any) -> None:
        """Add an item to the circular queue."""
        if self.is_full():
            raise OverflowError("Queue is full")
        
        if self.is_empty():
            self._front = self._rear = 0
        else:
            self._rear = (self._rear + 1) % self._capacity
        
        self._items[self._rear] = item
        self._size += 1
        if self._debug:
            print(f"Enqueued {item} at position {self._rear}. Size: {self._size}")
    
    def dequeue(self) -> Any:
        """Remove and return the front item from the circular queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        
        item = self._items[self._front]
        self._items[self._front] = None
        
        if self._size == 1:  # Last item
            self._front = self._rear = -1
        else:
            self._front = (self._front + 1) % self._capacity
        
        self._size -= 1
        if self._debug:
            print(f"Dequeued {item}. Size: {self._size}")
        return item
    
    def front(self) -> Any:
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Front of empty queue")
        return self._items[self._front]
    
    def rear(self) -> Any:
        """Return the rear item without removing it."""
        if self.is_empty():
            raise IndexError("Rear of empty queue")
        return self._items[self._rear]
    
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return self._size == 0
    
    def is_full(self) -> bool:
        """Check if the queue is full."""
        return self._size == self._capacity
    
    def size(self) -> int:
        """Return the number of items in the queue."""
        return self._size
    
    def capacity(self) -> int:
        """Return the maximum capacity of the queue."""
        return self._capacity
    
    def to_list(self) -> list:
        """Return queue contents as a list (front to rear)."""
        if self.is_empty():
            return []
        
        result = []
        current = self._front
        for _ in range(self._size):
            result.append(self._items[current])
            current = (current + 1) % self._capacity
        return result
    
    def __str__(self) -> str:
        """String representation of the circular queue."""
        return f"CircularQueue({self.to_list()}, capacity={self._capacity})"


# ============================================================================
# DOUBLE-ENDED QUEUE (DEQUE)
# ============================================================================

class Deque:
    """Double-ended queue implementation using Python's deque."""
    
    def __init__(self, debug: bool = False):
        """Initialize an empty deque."""
        self._items = deque()
        self._debug = debug
        if self._debug:
            print("Deque initialized")
    
    def add_front(self, item: Any) -> None:
        """Add an item to the front of the deque."""
        self._items.appendleft(item)
        if self._debug:
            print(f"Added {item} to front. Size: {len(self._items)}")
    
    def add_rear(self, item: Any) -> None:
        """Add an item to the rear of the deque."""
        self._items.append(item)
        if self._debug:
            print(f"Added {item} to rear. Size: {len(self._items)}")
    
    def remove_front(self) -> Any:
        """Remove and return the front item from the deque."""
        if self.is_empty():
            raise IndexError("Remove from empty deque")
        item = self._items.popleft()
        if self._debug:
            print(f"Removed {item} from front. Size: {len(self._items)}")
        return item
    
    def remove_rear(self) -> Any:
        """Remove and return the rear item from the deque."""
        if self.is_empty():
            raise IndexError("Remove from empty deque")
        item = self._items.pop()
        if self._debug:
            print(f"Removed {item} from rear. Size: {len(self._items)}")
        return item
    
    def front(self) -> Any:
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Front of empty deque")
        return self._items[0]
    
    def rear(self) -> Any:
        """Return the rear item without removing it."""
        if self.is_empty():
            raise IndexError("Rear of empty deque")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """Check if the deque is empty."""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Return the number of items in the deque."""
        return len(self._items)
    
    def clear(self) -> None:
        """Remove all items from the deque."""
        self._items.clear()
        if self._debug:
            print("Deque cleared")
    
    def to_list(self) -> list:
        """Return deque contents as a list."""
        return list(self._items)
    
    def __str__(self) -> str:
        """String representation of the deque."""
        return f"Deque({list(self._items)})"


# ============================================================================
# PRIORITY QUEUE
# ============================================================================

class PriorityQueue:
    """Priority queue implementation using heapq."""
    
    def __init__(self, debug: bool = False):
        """Initialize an empty priority queue."""
        self._heap = []
        self._index = 0  # For stable ordering
        self._debug = debug
        if self._debug:
            print("PriorityQueue initialized")
    
    def enqueue(self, item: Any, priority: int) -> None:
        """Add an item with given priority (lower number = higher priority)."""
        heapq.heappush(self._heap, (priority, self._index, item))
        self._index += 1
        if self._debug:
            print(f"Enqueued {item} with priority {priority}. Size: {len(self._heap)}")
    
    def dequeue(self) -> Any:
        """Remove and return the highest priority item."""
        if self.is_empty():
            raise IndexError("Dequeue from empty priority queue")
        priority, _, item = heapq.heappop(self._heap)
        if self._debug:
            print(f"Dequeued {item} with priority {priority}. Size: {len(self._heap)}")
        return item
    
    def peek(self) -> Any:
        """Return the highest priority item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty priority queue")
        return self._heap[0][2]
    
    def is_empty(self) -> bool:
        """Check if the priority queue is empty."""
        return len(self._heap) == 0
    
    def size(self) -> int:
        """Return the number of items in the priority queue."""
        return len(self._heap)
    
    def clear(self) -> None:
        """Remove all items from the priority queue."""
        self._heap.clear()
        self._index = 0
        if self._debug:
            print("Priority queue cleared")
    
    def __str__(self) -> str:
        """String representation of the priority queue."""
        items = [(priority, item) for priority, _, item in self._heap]
        return f"PriorityQueue({items})"


# ============================================================================
# QUEUE APPLICATIONS
# ============================================================================

def generate_binary_numbers(n: int, debug: bool = False) -> list:
    """Generate first n binary numbers using queue."""
    if n <= 0:
        return []
    
    queue = LinkedListQueue(debug=debug)
    result = []
    
    queue.enqueue("1")
    if debug:
        print(f"Generating first {n} binary numbers:")
    
    for i in range(n):
        binary = queue.dequeue()
        result.append(binary)
        if debug:
            print(f"Generated: {binary}")
        
        # Generate next binary numbers
        queue.enqueue(binary + "0")
        queue.enqueue(binary + "1")
    
    return result


def hot_potato_simulation(names: list, num: int, debug: bool = False) -> str:
    """Hot potato elimination game using queue."""
    queue = LinkedListQueue(debug=debug)
    
    # Add all names to queue
    for name in names:
        queue.enqueue(name)
    
    if debug:
        print(f"Starting hot potato game with {names}, counting by {num}")
    
    while queue.size() > 1:
        # Pass the potato
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        
        # Eliminate current person
        eliminated = queue.dequeue()
        if debug:
            print(f"Eliminated: {eliminated}, Remaining: {queue.to_list()}")
    
    winner = queue.dequeue()
    if debug:
        print(f"Winner: {winner}")
    return winner


def task_scheduler(tasks: list, debug: bool = False) -> list:
    """Simple task scheduler using priority queue."""
    pq = PriorityQueue(debug=debug)
    
    # Add tasks with priorities
    for task, priority in tasks:
        pq.enqueue(task, priority)
    
    execution_order = []
    if debug:
        print("Executing tasks in priority order:")
    
    while not pq.is_empty():
        task = pq.dequeue()
        execution_order.append(task)
        if debug:
            print(f"Executing: {task}")
    
    return execution_order


# ============================================================================
# EXAMPLE USAGE AND TESTING
# ============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("Queue Data Structures Demo")
    print("=" * 50)
    
    # 1. Array Queue Demo
    print("\n1. Array Queue Demo:")
    array_queue = ArrayQueue(debug=True)
    for i in [10, 20, 30]:
        array_queue.enqueue(i)
    
    print(f"Queue: {array_queue}")
    print(f"Front: {array_queue.front()}")
    print(f"Dequeue: {array_queue.dequeue()}")
    
    # 2. Linked List Queue Demo
    print("\n2. Linked List Queue Demo:")
    ll_queue = LinkedListQueue(debug=True)
    for i in ['A', 'B', 'C']:
        ll_queue.enqueue(i)
    
    print(f"Queue: {ll_queue}")
    print(f"Rear: {ll_queue.rear()}")
    
    # 3. Circular Queue Demo
    print("\n3. Circular Queue Demo:")
    cq = CircularQueue(5, debug=True)
    for i in range(1, 6):
        cq.enqueue(i)
    
    print(f"Is full: {cq.is_full()}")
    cq.dequeue()
    cq.dequeue()
    cq.enqueue(6)
    print(f"Queue: {cq}")
    
    # 4. Deque Demo
    print("\n4. Deque Demo:")
    dq = Deque(debug=True)
    dq.add_front(2)
    dq.add_rear(3)
    dq.add_front(1)
    dq.add_rear(4)
    print(f"Deque: {dq}")
    
    # 5. Priority Queue Demo
    print("\n5. Priority Queue Demo:")
    pq = PriorityQueue(debug=True)
    tasks = [("Low priority task", 3), ("High priority task", 1), ("Medium priority task", 2)]
    for task, priority in tasks:
        pq.enqueue(task, priority)
    
    print("Execution order:")
    while not pq.is_empty():
        print(f"- {pq.dequeue()}")
    
    # 6. Binary Numbers Generation
    print("\n6. Binary Numbers Generation:")
    binary_nums = generate_binary_numbers(8, debug=True)
    print(f"First 8 binary numbers: {binary_nums}")
    
    # 7. Hot Potato Game
    print("\n7. Hot Potato Game:")
    players = ["Alice", "Bob", "Charlie", "David", "Eve"]
    winner = hot_potato_simulation(players, 3, debug=True)
    print(f"Game winner: {winner}")
    
    # 8. Task Scheduler
    print("\n8. Task Scheduler:")
    tasks = [("Email check", 2), ("System backup", 1), ("Report generation", 3)]
    order = task_scheduler(tasks, debug=True)
    print(f"Execution order: {order}")
