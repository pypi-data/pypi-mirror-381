"""
graph.py - DSA Toolkit

This module implements comprehensive graph data structures and algorithms:
- Graph representation (adjacency list, adjacency matrix)
- Depth First Search (DFS) and Breadth First Search (BFS)
- Cycle Detection (Undirected & Directed)
- Topological Sort
- Shortest Path Algorithms (Dijkstra, Bellman-Ford, Floyd-Warshall)
- Minimum Spanning Tree (Kruskal, Prim)
- Union-Find (Disjoint Set Union)
- Graph coloring and other algorithms

Features:
- Multiple graph representations
- Comprehensive pathfinding algorithms
- Optional debug tracing
- Weighted and unweighted graphs
"""

from collections import defaultdict, deque
from typing import List, Dict, Set, Tuple, Optional, Any
import heapq
import math


# ============================================================================
# GRAPH CLASS WITH ADJACENCY LIST
# ============================================================================

class Graph:
    """Graph implementation using adjacency list representation."""
    
    def __init__(self, directed: bool = False, debug: bool = False):
        """Initialize a graph."""
        self.graph = defaultdict(list)
        self.directed = directed
        self._debug = debug
        self.vertices = set()
        if self._debug:
            print(f"Graph initialized ({'directed' if directed else 'undirected'})")
    
    def add_vertex(self, vertex: Any) -> None:
        """Add a vertex to the graph."""
        self.vertices.add(vertex)
        if vertex not in self.graph:
            self.graph[vertex] = []
        if self._debug:
            print(f"Added vertex: {vertex}")
    
    def add_edge(self, u: Any, v: Any, weight: int = 1) -> None:
        """Add an edge to the graph."""
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))
        if self._debug:
            direction = "->" if self.directed else "<->"
            print(f"Added edge: {u} {direction} {v} (weight: {weight})")
    
    def remove_edge(self, u: Any, v: Any) -> bool:
        """Remove an edge from the graph."""
        removed = False
        if u in self.graph:
            self.graph[u] = [(vertex, weight) for vertex, weight in self.graph[u] if vertex != v]
            removed = True
        
        if not self.directed and v in self.graph:
            self.graph[v] = [(vertex, weight) for vertex, weight in self.graph[v] if vertex != u]
        
        if self._debug and removed:
            print(f"Removed edge: {u} -> {v}")
        return removed
    
    def get_neighbors(self, vertex: Any) -> List[Tuple[Any, int]]:
        """Get neighbors of a vertex."""
        return self.graph.get(vertex, [])
    
    def get_vertices(self) -> Set[Any]:
        """Get all vertices in the graph."""
        return self.vertices.copy()
    
    def get_edges(self) -> List[Tuple[Any, Any, int]]:
        """Get all edges in the graph."""
        edges = []
        for u in self.graph:
            for v, weight in self.graph[u]:
                if self.directed or (u, v, weight) not in edges and (v, u, weight) not in edges:
                    edges.append((u, v, weight))
        return edges
    
    def vertex_count(self) -> int:
        """Get number of vertices."""
        return len(self.vertices)
    
    def edge_count(self) -> int:
        """Get number of edges."""
        total = sum(len(neighbors) for neighbors in self.graph.values())
        return total if self.directed else total // 2
    
    def dfs_recursive(self, start: Any, visited: Set[Any] = None) -> List[Any]:
        """Depth First Search (recursive implementation)."""
        if visited is None:
            visited = set()
        
        visited.add(start)
        result = [start]
        if self._debug:
            print(f"DFS visiting: {start}")
        
        for neighbor, _ in self.graph[start]:
            if neighbor not in visited:
                result.extend(self.dfs_recursive(neighbor, visited))
        
        return result
    
    def dfs_iterative(self, start: Any) -> List[Any]:
        """Depth First Search (iterative implementation)."""
        visited = set()
        stack = [start]
        result = []
        
        if self._debug:
            print("Starting DFS (iterative)")
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                if self._debug:
                    print(f"DFS visiting: {vertex}")
                
                # Add neighbors to stack (reverse order for correct traversal)
                for neighbor, _ in reversed(self.graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result
    
    def bfs(self, start: Any) -> List[Any]:
        """Breadth First Search implementation."""
        visited = set([start])
        queue = deque([start])
        result = []
        
        if self._debug:
            print("Starting BFS")
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            if self._debug:
                print(f"BFS visiting: {vertex}")
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def shortest_path_bfs(self, start: Any, end: Any) -> Optional[List[Any]]:
        """Find shortest path between two vertices using BFS (unweighted)."""
        if start == end:
            return [start]
        
        visited = set([start])
        queue = deque([(start, [start])])
        
        if self._debug:
            print(f"Finding shortest path from {start} to {end}")
        
        while queue:
            vertex, path = queue.popleft()
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor == end:
                    if self._debug:
                        print(f"Path found: {path + [neighbor]}")
                    return path + [neighbor]
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        if self._debug:
            print("No path found")
        return None
    
    def has_cycle_undirected(self) -> bool:
        """Detect cycle in undirected graph using DFS."""
        visited = set()
        
        def dfs_cycle(vertex, parent):
            visited.add(vertex)
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    if dfs_cycle(neighbor, vertex):
                        return True
                elif neighbor != parent:
                    if self._debug:
                        print(f"Cycle detected: {vertex} -> {neighbor}")
                    return True
            return False
        
        for vertex in self.vertices:
            if vertex not in visited:
                if dfs_cycle(vertex, None):
                    return True
        return False
    
    def has_cycle_directed(self) -> bool:
        """Detect cycle in directed graph using DFS."""
        visited = set()
        rec_stack = set()
        
        def dfs_cycle(vertex):
            visited.add(vertex)
            rec_stack.add(vertex)
            
            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    if dfs_cycle(neighbor):
                        return True
                elif neighbor in rec_stack:
                    if self._debug:
                        print(f"Cycle detected: {vertex} -> {neighbor}")
                    return True
            
            rec_stack.remove(vertex)
            return False
        
        for vertex in self.vertices:
            if vertex not in visited:
                if dfs_cycle(vertex):
                    return True
        return False
    
    def topological_sort(self) -> List[Any]:
        """Topological sort using Kahn's algorithm."""
        if not self.directed:
            raise ValueError("Topological sort only works on directed graphs")
        
        in_degree = {vertex: 0 for vertex in self.vertices}
        
        # Calculate in-degrees
        for vertex in self.graph:
            for neighbor, _ in self.graph[vertex]:
                in_degree[neighbor] += 1
        
        # Find vertices with no incoming edges
        queue = deque([vertex for vertex in self.vertices if in_degree[vertex] == 0])
        result = []
        
        if self._debug:
            print(f"Starting topological sort. Initial queue: {list(queue)}")
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            if self._debug:
                print(f"Processing vertex: {vertex}")
            
            for neighbor, _ in self.graph[vertex]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    if self._debug:
                        print(f"Added to queue: {neighbor}")
        
        if len(result) != len(self.vertices):
            if self._debug:
                print("Cycle detected - topological sort not possible")
            return []  # Cycle exists
        
        return result
    
    def dijkstra(self, start: Any) -> Dict[Any, Tuple[int, List[Any]]]:
        """Dijkstra's algorithm for shortest paths from a source vertex."""
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        previous = {vertex: None for vertex in self.vertices}
        priority_queue = [(0, start)]
        visited = set()
        
        if self._debug:
            print(f"Starting Dijkstra's algorithm from {start}")
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)
            if self._debug:
                print(f"Processing vertex: {current_vertex} (distance: {current_distance})")
            
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))
                    if self._debug:
                        print(f"Updated distance to {neighbor}: {distance}")
        
        # Reconstruct paths
        paths = {}
        for vertex in self.vertices:
            if distances[vertex] != float('inf'):
                path = []
                current = vertex
                while current is not None:
                    path.append(current)
                    current = previous[current]
                path.reverse()
                paths[vertex] = (distances[vertex], path)
            else:
                paths[vertex] = (float('inf'), [])
        
        return paths
    
    def bellman_ford(self, start: Any) -> Optional[Dict[Any, Tuple[int, List[Any]]]]:
        """Bellman-Ford algorithm for shortest paths (handles negative weights)."""
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        previous = {vertex: None for vertex in self.vertices}
        
        if self._debug:
            print(f"Starting Bellman-Ford algorithm from {start}")
        
        # Relax edges |V| - 1 times
        for i in range(len(self.vertices) - 1):
            if self._debug:
                print(f"Iteration {i + 1}")
            
            for u in self.graph:
                for v, weight in self.graph[u]:
                    if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
                        previous[v] = u
                        if self._debug:
                            print(f"Updated distance to {v}: {distances[v]}")
        
        # Check for negative weight cycles
        for u in self.graph:
            for v, weight in self.graph[u]:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    if self._debug:
                        print("Negative weight cycle detected")
                    return None  # Negative cycle exists
        
        # Reconstruct paths
        paths = {}
        for vertex in self.vertices:
            if distances[vertex] != float('inf'):
                path = []
                current = vertex
                while current is not None:
                    path.append(current)
                    current = previous[current]
                path.reverse()
                paths[vertex] = (distances[vertex], path)
            else:
                paths[vertex] = (float('inf'), [])
        
        return paths
    
    def print_graph(self) -> None:
        """Print the graph representation."""
        print(f"Graph ({'Directed' if self.directed else 'Undirected'}):")
        for vertex in sorted(self.vertices):
            neighbors = [f"{neighbor}({weight})" for neighbor, weight in self.graph[vertex]]
            print(f"  {vertex}: {neighbors}")


# ============================================================================
# ADJACENCY MATRIX GRAPH
# ============================================================================

class MatrixGraph:
    """Graph implementation using adjacency matrix representation."""
    
    def __init__(self, vertices: List[Any], directed: bool = False, debug: bool = False):
        """Initialize a graph with adjacency matrix."""
        self.vertices = vertices
        self.vertex_map = {vertex: i for i, vertex in enumerate(vertices)}
        self.directed = directed
        self._debug = debug
        self.size = len(vertices)
        self.matrix = [[0 for _ in range(self.size)] for _ in range(self.size)]
        
        if self._debug:
            print(f"MatrixGraph initialized with {self.size} vertices")
    
    def add_edge(self, u: Any, v: Any, weight: int = 1) -> None:
        """Add an edge to the graph."""
        if u not in self.vertex_map or v not in self.vertex_map:
            raise ValueError("Vertex not found in graph")
        
        u_idx = self.vertex_map[u]
        v_idx = self.vertex_map[v]
        
        self.matrix[u_idx][v_idx] = weight
        if not self.directed:
            self.matrix[v_idx][u_idx] = weight
        
        if self._debug:
            direction = "->" if self.directed else "<->"
            print(f"Added edge: {u} {direction} {v} (weight: {weight})")
    
    def remove_edge(self, u: Any, v: Any) -> None:
        """Remove an edge from the graph."""
        if u not in self.vertex_map or v not in self.vertex_map:
            raise ValueError("Vertex not found in graph")
        
        u_idx = self.vertex_map[u]
        v_idx = self.vertex_map[v]
        
        self.matrix[u_idx][v_idx] = 0
        if not self.directed:
            self.matrix[v_idx][u_idx] = 0
        
        if self._debug:
            print(f"Removed edge: {u} -> {v}")
    
    def has_edge(self, u: Any, v: Any) -> bool:
        """Check if there's an edge between two vertices."""
        if u not in self.vertex_map or v not in self.vertex_map:
            return False
        return self.matrix[self.vertex_map[u]][self.vertex_map[v]] != 0
    
    def get_weight(self, u: Any, v: Any) -> int:
        """Get the weight of an edge."""
        if u not in self.vertex_map or v not in self.vertex_map:
            return 0
        return self.matrix[self.vertex_map[u]][self.vertex_map[v]]
    
    def floyd_warshall(self) -> Tuple[List[List[int]], List[List[Optional[Any]]]]:
        """Floyd-Warshall algorithm for all-pairs shortest paths."""
        # Initialize distance matrix
        dist = [[float('inf') for _ in range(self.size)] for _ in range(self.size)]
        next_vertex = [[None for _ in range(self.size)] for _ in range(self.size)]
        
        # Initialize with direct edges
        for i in range(self.size):
            for j in range(self.size):
                if i == j:
                    dist[i][j] = 0
                elif self.matrix[i][j] != 0:
                    dist[i][j] = self.matrix[i][j]
                    next_vertex[i][j] = self.vertices[j]
        
        if self._debug:
            print("Starting Floyd-Warshall algorithm")
        
        # Floyd-Warshall algorithm
        for k in range(self.size):
            if self._debug:
                print(f"Processing intermediate vertex: {self.vertices[k]}")
            
            for i in range(self.size):
                for j in range(self.size):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_vertex[i][j] = next_vertex[i][k]
        
        return dist, next_vertex
    
    def reconstruct_path(self, start: Any, end: Any, next_matrix: List[List[Optional[Any]]]) -> List[Any]:
        """Reconstruct path from Floyd-Warshall next matrix."""
        if start not in self.vertex_map or end not in self.vertex_map:
            return []
        
        start_idx = self.vertex_map[start]
        end_idx = self.vertex_map[end]
        
        if next_matrix[start_idx][end_idx] is None:
            return []
        
        path = [start]
        current = start
        while current != end:
            current = next_matrix[self.vertex_map[current]][end_idx]
            path.append(current)
        
        return path
    
    def print_matrix(self) -> None:
        """Print the adjacency matrix."""
        print("Adjacency Matrix:")
        print("   ", end="")
        for vertex in self.vertices:
            print(f"{vertex:4}", end="")
        print()
        
        for i, vertex in enumerate(self.vertices):
            print(f"{vertex:2} ", end="")
            for j in range(self.size):
                print(f"{self.matrix[i][j]:4}", end="")
            print()


# ============================================================================
# UNION-FIND (DISJOINT SET UNION)
# ============================================================================

class UnionFind:
    """Union-Find data structure with path compression and union by rank."""
    
    def __init__(self, vertices: List[Any], debug: bool = False):
        """Initialize Union-Find structure."""
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}
        self._debug = debug
        if self._debug:
            print(f"UnionFind initialized with {len(vertices)} vertices")
    
    def find(self, x: Any) -> Any:
        """Find the root of x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x: Any, y: Any) -> bool:
        """Union two sets by rank."""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already in same set
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        if self._debug:
            print(f"United {x} and {y}")
        return True
    
    def connected(self, x: Any, y: Any) -> bool:
        """Check if two vertices are in the same component."""
        return self.find(x) == self.find(y)


# ============================================================================
# MINIMUM SPANNING TREE ALGORITHMS
# ============================================================================

def kruskal_mst(graph: Graph, debug: bool = False) -> List[Tuple[Any, Any, int]]:
    """Kruskal's algorithm for Minimum Spanning Tree."""
    edges = graph.get_edges()
    edges.sort(key=lambda x: x[2])  # Sort by weight
    
    vertices = list(graph.get_vertices())
    uf = UnionFind(vertices, debug)
    mst = []
    total_weight = 0
    
    if debug:
        print("Starting Kruskal's MST algorithm")
        print(f"Sorted edges: {edges}")
    
    for u, v, weight in edges:
        if not uf.connected(u, v):
            uf.union(u, v)
            mst.append((u, v, weight))
            total_weight += weight
            if debug:
                print(f"Added edge to MST: {u} - {v} (weight: {weight})")
            
            if len(mst) == len(vertices) - 1:
                break
    
    if debug:
        print(f"MST total weight: {total_weight}")
    
    return mst


def prim_mst(graph: Graph, start: Any = None, debug: bool = False) -> List[Tuple[Any, Any, int]]:
    """Prim's algorithm for Minimum Spanning Tree."""
    vertices = graph.get_vertices()
    if not vertices:
        return []
    
    if start is None:
        start = next(iter(vertices))
    
    mst = []
    visited = {start}
    edges = []
    
    if debug:
        print(f"Starting Prim's MST algorithm from {start}")
    
    # Add all edges from start vertex
    for neighbor, weight in graph.get_neighbors(start):
        heapq.heappush(edges, (weight, start, neighbor))
    
    while edges and len(visited) < len(vertices):
        weight, u, v = heapq.heappop(edges)
        
        if v in visited:
            continue
        
        visited.add(v)
        mst.append((u, v, weight))
        if debug:
            print(f"Added edge to MST: {u} - {v} (weight: {weight})")
        
        # Add edges from newly visited vertex
        for neighbor, edge_weight in graph.get_neighbors(v):
            if neighbor not in visited:
                heapq.heappush(edges, (edge_weight, v, neighbor))
    
    return mst


# ============================================================================
# GRAPH COLORING
# ============================================================================

def graph_coloring_greedy(graph: Graph, debug: bool = False) -> Dict[Any, int]:
    """Greedy graph coloring algorithm."""
    vertices = list(graph.get_vertices())
    colors = {}
    
    if debug:
        print("Starting greedy graph coloring")
    
    for vertex in vertices:
        # Find the smallest color not used by neighbors
        neighbor_colors = set()
        for neighbor, _ in graph.get_neighbors(vertex):
            if neighbor in colors:
                neighbor_colors.add(colors[neighbor])
        
        color = 0
        while color in neighbor_colors:
            color += 1
        
        colors[vertex] = color
        if debug:
            print(f"Colored vertex {vertex} with color {color}")
    
    return colors


# ============================================================================
# GRAPH ANALYSIS FUNCTIONS
# ============================================================================

def is_bipartite(graph: Graph, debug: bool = False) -> bool:
    """Check if a graph is bipartite using BFS coloring."""
    vertices = graph.get_vertices()
    if not vertices:
        return True
    
    colors = {}
    
    for start in vertices:
        if start in colors:
            continue
        
        queue = deque([start])
        colors[start] = 0
        
        while queue:
            vertex = queue.popleft()
            current_color = colors[vertex]
            
            for neighbor, _ in graph.get_neighbors(vertex):
                if neighbor in colors:
                    if colors[neighbor] == current_color:
                        if debug:
                            print(f"Not bipartite: {vertex} and {neighbor} have same color")
                        return False
                else:
                    colors[neighbor] = 1 - current_color
                    queue.append(neighbor)
    
    if debug:
        print("Graph is bipartite")
    return True


def strongly_connected_components(graph: Graph, debug: bool = False) -> List[List[Any]]:
    """Find strongly connected components using Kosaraju's algorithm."""
    if not graph.directed:
        raise ValueError("SCC only applies to directed graphs")
    
    vertices = list(graph.get_vertices())
    visited = set()
    finish_order = []
    
    # Step 1: DFS to get finish times
    def dfs1(vertex):
        visited.add(vertex)
        for neighbor, _ in graph.get_neighbors(vertex):
            if neighbor not in visited:
                dfs1(neighbor)
        finish_order.append(vertex)
    
    for vertex in vertices:
        if vertex not in visited:
            dfs1(vertex)
    
    # Step 2: Create transpose graph
    transpose = Graph(directed=True, debug=debug)
    for vertex in vertices:
        transpose.add_vertex(vertex)
    
    for u in graph.graph:
        for v, weight in graph.graph[u]:
            transpose.add_edge(v, u, weight)
    
    # Step 3: DFS on transpose in reverse finish order
    visited = set()
    sccs = []
    
    def dfs2(vertex, component):
        visited.add(vertex)
        component.append(vertex)
        for neighbor, _ in transpose.get_neighbors(vertex):
            if neighbor not in visited:
                dfs2(neighbor, component)
    
    for vertex in reversed(finish_order):
        if vertex not in visited:
            component = []
            dfs2(vertex, component)
            sccs.append(component)
            if debug:
                print(f"SCC found: {component}")
    
    return sccs


# ============================================================================
# EXAMPLE USAGE AND TESTING
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("Graph Data Structures and Algorithms Demo")
    print("=" * 70)
    
    # 1. Basic Graph Operations
    print("\n1. Basic Graph Operations:")
    g = Graph(directed=False, debug=True)
    
    # Add vertices and edges
    edges = [('A', 'B', 4), ('A', 'C', 2), ('B', 'C', 1), ('B', 'D', 5), ('C', 'D', 8), ('C', 'E', 10), ('D', 'E', 2)]
    for u, v, w in edges:
        g.add_edge(u, v, w)
    
    g.print_graph()
    print(f"Vertices: {g.vertex_count()}, Edges: {g.edge_count()}")
    
    # 2. Graph Traversals
    print("\n2. Graph Traversals:")
    print(f"DFS from A: {g.dfs_recursive('A')}")
    print(f"BFS from A: {g.bfs('A')}")
    print(f"Shortest path A to E: {g.shortest_path_bfs('A', 'E')}")
    
    # 3. Cycle Detection
    print("\n3. Cycle Detection:")
    print(f"Has cycle (undirected): {g.has_cycle_undirected()}")
    
    # 4. Shortest Path Algorithms
    print("\n4. Shortest Path Algorithms:")
    paths = g.dijkstra('A')
    for vertex, (distance, path) in paths.items():
        if distance != float('inf'):
            print(f"A to {vertex}: distance={distance}, path={' -> '.join(path)}")
    
    # 5. Minimum Spanning Tree
    print("\n5. Minimum Spanning Tree:")
    mst_kruskal = kruskal_mst(g, debug=True)
    print(f"Kruskal MST: {mst_kruskal}")
    
    mst_prim = prim_mst(g, 'A', debug=True)
    print(f"Prim MST: {mst_prim}")
    
    # 6. Directed Graph Operations
    print("\n6. Directed Graph Operations:")
    dg = Graph(directed=True, debug=True)
    directed_edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('A', 'E')]
    for u, v in directed_edges:
        dg.add_edge(u, v)
    
    print(f"Has cycle (directed): {dg.has_cycle_directed()}")
    print(f"Topological sort: {dg.topological_sort()}")
    
    # 7. Matrix Graph Demo
    print("\n7. Matrix Graph Demo:")
    vertices = ['A', 'B', 'C', 'D']
    mg = MatrixGraph(vertices, debug=True)
    
    mg.add_edge('A', 'B', 1)
    mg.add_edge('A', 'C', 4)
    mg.add_edge('B', 'C', 2)
    mg.add_edge('B', 'D', 5)
    mg.add_edge('C', 'D', 1)
    
    mg.print_matrix()
    
    dist, next_matrix = mg.floyd_warshall()
    print(f"Shortest distance A to D: {dist[0][3]}")
    print(f"Path A to D: {' -> '.join(mg.reconstruct_path('A', 'D', next_matrix))}")
    
    # 8. Graph Analysis
    print("\n8. Graph Analysis:")
    print(f"Is bipartite: {is_bipartite(g, debug=True)}")
    
    # Graph coloring
    colors = graph_coloring_greedy(g, debug=True)
    print(f"Graph coloring: {colors}")
    print(f"Chromatic number: {max(colors.values()) + 1}")
    
    # 9. Strongly Connected Components
    print("\n9. Strongly Connected Components:")
    sccs = strongly_connected_components(dg, debug=True)
    print(f"SCCs: {sccs}")
