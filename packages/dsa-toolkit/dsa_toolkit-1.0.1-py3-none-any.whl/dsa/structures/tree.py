"""
tree.py - DSA Toolkit

This module implements various Tree data structures and algorithms:
- Binary Tree
- Binary Search Tree (BST)
- AVL Tree (Self-balancing BST)
- Tree traversals (Inorder, Preorder, Postorder, Level Order)
- Common tree operations and algorithms

Features:
- Insert, delete, search operations
- Various traversal methods
- Tree validation and properties
- Optional debug tracing
"""

from typing import Any, Optional, List, Tuple
from collections import deque


# ============================================================================
# BINARY TREE NODE
# ============================================================================

class TreeNode:
    """Node for binary tree structures."""
    
    def __init__(self, data: Any):
        self.data = data
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None
        self.height = 1  # For AVL tree
    
    def __str__(self) -> str:
        return str(self.data)


# ============================================================================
# BINARY TREE
# ============================================================================

class BinaryTree:
    """Binary Tree implementation with common operations."""
    
    def __init__(self, debug: bool = False):
        """Initialize an empty binary tree."""
        self.root: Optional[TreeNode] = None
        self._debug = debug
        if self._debug:
            print("BinaryTree initialized")
    
    def insert_level_order(self, data: Any) -> None:
        """Insert node in level order (complete binary tree)."""
        new_node = TreeNode(data)
        
        if not self.root:
            self.root = new_node
            if self._debug:
                print(f"Inserted {data} as root")
            return
        
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            
            if not node.left:
                node.left = new_node
                if self._debug:
                    print(f"Inserted {data} as left child of {node.data}")
                return
            elif not node.right:
                node.right = new_node
                if self._debug:
                    print(f"Inserted {data} as right child of {node.data}")
                return
            else:
                queue.append(node.left)
                queue.append(node.right)
    
    def inorder_traversal(self, node: Optional[TreeNode] = None, result: List[Any] = None) -> List[Any]:
        """Inorder traversal: Left -> Root -> Right."""
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            if self._debug:
                print(f"Visiting: {node.data}")
            self.inorder_traversal(node.right, result)
        
        return result
    
    def preorder_traversal(self, node: Optional[TreeNode] = None, result: List[Any] = None) -> List[Any]:
        """Preorder traversal: Root -> Left -> Right."""
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            result.append(node.data)
            if self._debug:
                print(f"Visiting: {node.data}")
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
        
        return result
    
    def postorder_traversal(self, node: Optional[TreeNode] = None, result: List[Any] = None) -> List[Any]:
        """Postorder traversal: Left -> Right -> Root."""
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.data)
            if self._debug:
                print(f"Visiting: {node.data}")
        
        return result
    
    def level_order_traversal(self) -> List[Any]:
        """Level order traversal (BFS)."""
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append(node.data)
            if self._debug:
                print(f"Visiting: {node.data}")
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def height(self, node: Optional[TreeNode] = None) -> int:
        """Calculate the height of the tree."""
        if node is None:
            node = self.root
        
        if not node:
            return 0
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        return 1 + max(left_height, right_height)
    
    def count_nodes(self, node: Optional[TreeNode] = None) -> int:
        """Count total number of nodes in the tree."""
        if node is None:
            node = self.root
        
        if not node:
            return 0
        
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)
    
    def count_leaf_nodes(self, node: Optional[TreeNode] = None) -> int:
        """Count the number of leaf nodes."""
        if node is None:
            node = self.root
        
        if not node:
            return 0
        
        if not node.left and not node.right:
            return 1
        
        return self.count_leaf_nodes(node.left) + self.count_leaf_nodes(node.right)
    
    def is_balanced(self, node: Optional[TreeNode] = None) -> bool:
        """Check if the tree is height-balanced."""
        def check_balance(node):
            if not node:
                return True, 0
            
            left_balanced, left_height = check_balance(node.left)
            right_balanced, right_height = check_balance(node.right)
            
            balanced = (left_balanced and right_balanced and 
                       abs(left_height - right_height) <= 1)
            height = 1 + max(left_height, right_height)
            
            return balanced, height
        
        if node is None:
            node = self.root
        
        balanced, _ = check_balance(node)
        return balanced
    
    def print_tree(self, node: Optional[TreeNode] = None, prefix: str = "", is_last: bool = True) -> None:
        """Print tree structure visually."""
        if node is None:
            node = self.root
        
        if node:
            print(prefix + ("└── " if is_last else "├── ") + str(node.data))
            
            children = []
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
            
            for i, child in enumerate(children):
                is_last_child = i == len(children) - 1
                extension = "    " if is_last else "│   "
                self.print_tree(child, prefix + extension, is_last_child)


# ============================================================================
# BINARY SEARCH TREE (BST)
# ============================================================================

class BinarySearchTree(BinaryTree):
    """Binary Search Tree implementation."""
    
    def __init__(self, debug: bool = False):
        """Initialize an empty BST."""
        super().__init__(debug)
        if self._debug:
            print("BinarySearchTree initialized")
    
    def insert(self, data: Any) -> None:
        """Insert a new node maintaining BST property."""
        self.root = self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node: Optional[TreeNode], data: Any) -> TreeNode:
        """Recursive helper for insertion."""
        if not node:
            if self._debug:
                print(f"Inserting {data}")
            return TreeNode(data)
        
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        else:
            if self._debug:
                print(f"Duplicate value {data} not inserted")
        
        return node
    
    def search(self, data: Any) -> bool:
        """Search for a value in the BST."""
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node: Optional[TreeNode], data: Any) -> bool:
        """Recursive helper for search."""
        if not node:
            if self._debug:
                print(f"Value {data} not found")
            return False
        
        if self._debug:
            print(f"Searching: current node = {node.data}")
        
        if data == node.data:
            if self._debug:
                print(f"Found {data}")
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
    
    def delete(self, data: Any) -> None:
        """Delete a node from the BST."""
        self.root = self._delete_recursive(self.root, data)
    
    def _delete_recursive(self, node: Optional[TreeNode], data: Any) -> Optional[TreeNode]:
        """Recursive helper for deletion."""
        if not node:
            if self._debug:
                print(f"Value {data} not found for deletion")
            return None
        
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:  # Found the node to delete
            if self._debug:
                print(f"Deleting {data}")
            
            # Case 1: No children (leaf node)
            if not node.left and not node.right:
                return None
            
            # Case 2: One child
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            
            # Case 3: Two children
            # Find inorder successor (smallest in right subtree)
            successor = self._find_min(node.right)
            node.data = successor.data
            node.right = self._delete_recursive(node.right, successor.data)
        
        return node
    
    def _find_min(self, node: TreeNode) -> TreeNode:
        """Find the minimum value node in a subtree."""
        while node.left:
            node = node.left
        return node
    
    def _find_max(self, node: TreeNode) -> TreeNode:
        """Find the maximum value node in a subtree."""
        while node.right:
            node = node.right
        return node
    
    def find_min(self) -> Optional[Any]:
        """Find the minimum value in the BST."""
        if not self.root:
            return None
        return self._find_min(self.root).data
    
    def find_max(self) -> Optional[Any]:
        """Find the maximum value in the BST."""
        if not self.root:
            return None
        return self._find_max(self.root).data
    
    def is_valid_bst(self, node: Optional[TreeNode] = None, min_val: float = float('-inf'), max_val: float = float('inf')) -> bool:
        """Validate if the tree is a valid BST."""
        if node is None:
            node = self.root
        
        if not node:
            return True
        
        if node.data <= min_val or node.data >= max_val:
            if self._debug:
                print(f"BST property violated at node {node.data}")
            return False
        
        return (self.is_valid_bst(node.left, min_val, node.data) and
                self.is_valid_bst(node.right, node.data, max_val))
    
    def kth_smallest(self, k: int) -> Optional[Any]:
        """Find the kth smallest element in the BST."""
        def inorder_kth(node, counter):
            if not node:
                return None
            
            # Search left subtree
            result = inorder_kth(node.left, counter)
            if result is not None:
                return result
            
            # Visit current node
            counter[0] += 1
            if counter[0] == k:
                return node.data
            
            # Search right subtree
            return inorder_kth(node.right, counter)
        
        counter = [0]
        return inorder_kth(self.root, counter)


# ============================================================================
# AVL TREE (SELF-BALANCING BST)
# ============================================================================

class AVLTree:
    """AVL Tree (self-balancing binary search tree) implementation."""
    
    def __init__(self, debug: bool = False):
        """Initialize an empty AVL tree."""
        self.root: Optional[TreeNode] = None
        self._debug = debug
        if self._debug:
            print("AVLTree initialized")
    
    def _get_height(self, node: Optional[TreeNode]) -> int:
        """Get the height of a node."""
        if not node:
            return 0
        return node.height
    
    def _update_height(self, node: TreeNode) -> None:
        """Update the height of a node."""
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
    
    def _get_balance(self, node: Optional[TreeNode]) -> int:
        """Get the balance factor of a node."""
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _rotate_right(self, y: TreeNode) -> TreeNode:
        """Perform right rotation."""
        if self._debug:
            print(f"Right rotation at {y.data}")
        
        x = y.left
        t2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = t2
        
        # Update heights
        self._update_height(y)
        self._update_height(x)
        
        return x
    
    def _rotate_left(self, x: TreeNode) -> TreeNode:
        """Perform left rotation."""
        if self._debug:
            print(f"Left rotation at {x.data}")
        
        y = x.right
        t2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = t2
        
        # Update heights
        self._update_height(x)
        self._update_height(y)
        
        return y
    
    def insert(self, data: Any) -> None:
        """Insert a new node maintaining AVL property."""
        self.root = self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node: Optional[TreeNode], data: Any) -> TreeNode:
        """Recursive helper for AVL insertion."""
        # Step 1: Perform normal BST insertion
        if not node:
            if self._debug:
                print(f"Inserting {data}")
            return TreeNode(data)
        
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        else:  # Duplicate values not allowed
            if self._debug:
                print(f"Duplicate value {data} not inserted")
            return node
        
        # Step 2: Update height of current node
        self._update_height(node)
        
        # Step 3: Get the balance factor
        balance = self._get_balance(node)
        
        # Step 4: If unbalanced, perform rotations
        # Left Left Case
        if balance > 1 and data < node.left.data:
            if self._debug:
                print("Left Left case")
            return self._rotate_right(node)
        
        # Right Right Case
        if balance < -1 and data > node.right.data:
            if self._debug:
                print("Right Right case")
            return self._rotate_left(node)
        
        # Left Right Case
        if balance > 1 and data > node.left.data:
            if self._debug:
                print("Left Right case")
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Right Left Case
        if balance < -1 and data < node.right.data:
            if self._debug:
                print("Right Left case")
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def inorder_traversal(self) -> List[Any]:
        """Inorder traversal of AVL tree."""
        def inorder(node, result):
            if node:
                inorder(node.left, result)
                result.append(node.data)
                inorder(node.right, result)
        
        result = []
        inorder(self.root, result)
        return result
    
    def print_tree(self, node: Optional[TreeNode] = None, prefix: str = "", is_last: bool = True) -> None:
        """Print AVL tree structure with heights."""
        if node is None:
            node = self.root
        
        if node:
            print(prefix + ("└── " if is_last else "├── ") + f"{node.data} (h={node.height})")
            
            children = []
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
            
            for i, child in enumerate(children):
                is_last_child = i == len(children) - 1
                extension = "    " if is_last else "│   "
                self.print_tree(child, prefix + extension, is_last_child)


# ============================================================================
# TREE ALGORITHMS
# ============================================================================

def tree_from_preorder_inorder(preorder: List[Any], inorder: List[Any], debug: bool = False) -> Optional[TreeNode]:
    """Construct binary tree from preorder and inorder traversals."""
    if not preorder or not inorder:
        return None
    
    root_val = preorder[0]
    root = TreeNode(root_val)
    
    if debug:
        print(f"Creating node: {root_val}")
    
    if len(preorder) == 1:
        return root
    
    # Find root position in inorder
    root_index = inorder.index(root_val)
    
    # Split arrays
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]
    left_preorder = preorder[1:1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder):]
    
    # Recursively build subtrees
    root.left = tree_from_preorder_inorder(left_preorder, left_inorder, debug)
    root.right = tree_from_preorder_inorder(right_preorder, right_inorder, debug)
    
    return root


def lowest_common_ancestor(root: Optional[TreeNode], p: Any, q: Any, debug: bool = False) -> Optional[TreeNode]:
    """Find the lowest common ancestor of two nodes in a BST."""
    if not root:
        return None
    
    if debug:
        print(f"Checking node: {root.data}")
    
    # If both p and q are smaller than root, LCA lies in left subtree
    if p < root.data and q < root.data:
        return lowest_common_ancestor(root.left, p, q, debug)
    
    # If both p and q are greater than root, LCA lies in right subtree
    if p > root.data and q > root.data:
        return lowest_common_ancestor(root.right, p, q, debug)
    
    # If one is on left and other on right, root is LCA
    if debug:
        print(f"LCA found: {root.data}")
    return root


def diameter_of_tree(root: Optional[TreeNode], debug: bool = False) -> int:
    """Find the diameter (longest path) of a binary tree."""
    def diameter_helper(node):
        if not node:
            return 0, 0  # height, diameter
        
        left_height, left_diameter = diameter_helper(node.left)
        right_height, right_diameter = diameter_helper(node.right)
        
        current_height = 1 + max(left_height, right_height)
        current_diameter = max(left_diameter, right_diameter, left_height + right_height)
        
        if debug:
            print(f"Node {node.data}: height={current_height}, diameter={current_diameter}")
        
        return current_height, current_diameter
    
    _, diameter = diameter_helper(root)
    return diameter


# ============================================================================
# EXAMPLE USAGE AND TESTING
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("Tree Data Structures Demo")
    print("=" * 60)
    
    # 1. Binary Tree Demo
    print("\n1. Binary Tree Demo:")
    bt = BinaryTree(debug=True)
    
    # Insert nodes in level order
    for val in [1, 2, 3, 4, 5, 6, 7]:
        bt.insert_level_order(val)
    
    print(f"Inorder: {bt.inorder_traversal()}")
    print(f"Preorder: {bt.preorder_traversal()}")
    print(f"Postorder: {bt.postorder_traversal()}")
    print(f"Level order: {bt.level_order_traversal()}")
    print(f"Height: {bt.height()}")
    print(f"Total nodes: {bt.count_nodes()}")
    print(f"Leaf nodes: {bt.count_leaf_nodes()}")
    print(f"Is balanced: {bt.is_balanced()}")
    
    print("\nTree structure:")
    bt.print_tree()
    
    # 2. Binary Search Tree Demo
    print("\n2. Binary Search Tree Demo:")
    bst = BinarySearchTree(debug=True)
    
    # Insert values
    values = [50, 30, 20, 40, 70, 60, 80]
    for val in values:
        bst.insert(val)
    
    print(f"Inorder (sorted): {bst.inorder_traversal()}")
    print(f"Is valid BST: {bst.is_valid_bst()}")
    print(f"Min value: {bst.find_min()}")
    print(f"Max value: {bst.find_max()}")
    
    # Search operations
    print(f"Search 40: {bst.search(40)}")
    print(f"Search 90: {bst.search(90)}")
    
    # Find kth smallest
    print(f"3rd smallest: {bst.kth_smallest(3)}")
    
    print("\nBST structure:")
    bst.print_tree()
    
    # Delete operations
    print(f"\nDeleting 20 (leaf):")
    bst.delete(20)
    print(f"Inorder after deletion: {bst.inorder_traversal()}")
    
    # 3. AVL Tree Demo
    print("\n3. AVL Tree Demo:")
    avl = AVLTree(debug=True)
    
    # Insert values that would cause imbalance in regular BST
    values = [10, 20, 30, 40, 50, 25]
    for val in values:
        avl.insert(val)
    
    print(f"AVL inorder: {avl.inorder_traversal()}")
    print("\nAVL tree structure (with heights):")
    avl.print_tree()
    
    # 4. Tree Construction Demo
    print("\n4. Tree Construction from Traversals:")
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    
    print(f"Preorder: {preorder}")
    print(f"Inorder: {inorder}")
    
    constructed_root = tree_from_preorder_inorder(preorder, inorder, debug=True)
    
    # Create a BinaryTree object to use traversal methods
    constructed_tree = BinaryTree()
    constructed_tree.root = constructed_root
    print(f"Constructed tree inorder: {constructed_tree.inorder_traversal()}")
    
    # 5. Tree Algorithms Demo
    print("\n5. Tree Algorithms Demo:")

    # LCA demo
    print(f"LCA of 60 and 80 in BST: {lowest_common_ancestor(bst.root, 60, 80, debug=True).data}")

    # Diameter demo
    print(f"Diameter of binary tree: {diameter_of_tree(bt.root, debug=True)}")
