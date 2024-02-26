"""Graph Data Structure implementation based on Python dicts."""

from collections import namedtuple, deque


AdjacentNeighbor = namedtuple("AdjacentNeighbor", "node weight")

class Graph:
    """Directed or Undirected simple or weighted graph class."""

    def __init__(self, vertices: list, directed: bool=False) -> None:
        
        self._vertices = dict.fromkeys(vertices)
        for key in self._vertices:
            self._vertices[key] = []

        self._directed = directed

    def __str__(self):
        message = []
        for key, value in self._vertices.items():
            message.append(f"{key} -> {[f'{k}({w})' for k, w in value]}")
        
        return "\n".join(message)

    def contains_edge(self, start, end):
        if start not in self._vertices:
            return False
        
        for adj, _ in self._vertices[start]:
            if adj == end:
                return True
        
        return False
    
    def add_edge(self, start, end, weight=1):

        if start not in self._vertices:
            print(f"Node {start} does not exist.")
            return
        
        if end not in self._vertices:
            print(f"Node {end} does not exist.")
            return
        
        if self.contains_edge(start, end):
            print(f"Edge {start} -> {end} exists already.")
            return
        
        self._vertices[start].append(AdjacentNeighbor(end, weight))

        if not self._directed:
            self._vertices[end].append(AdjacentNeighbor(start, weight))
       
    def remove_edge(self, start, end):

        if start not in self._vertices:
            print(f"Node {start} does not exist.")
            return
        
        if end not in self._vertices:
            print(f"Node {end} does not exist.")
            return
        
        for neighbor in self._vertices[start]:
            if neighbor.node == end:
                self._vertices[start].remove(neighbor)
                break
        else:
            print(f"Edge {start} -> {end} does not exist cannot be removed.")     

        if not self._directed:
            for neighbor in self._vertices[end]:
                if neighbor.node == start:
                    self._vertices[end].remove(neighbor)
                    break
            else:
                print(f"Edge {end} -> {start} does not exist cannot be removed.")  

    def bfs(self, start):
        if start not in self._vertices:
            print(f"Node {start} does not exist.")
            return
        
        q = deque()
        q.append(start)
        visited = set()
        path =[]

        while q:
            node = q.popleft()
            
            if node in visited:
                continue

            path.append(node)
            visited.add(node)

            for neighbor in self._vertices[node]:
                if neighbor.node in visited:
                    continue
                q.append(neighbor.node)
        
        return path
    
    def dfs(self, start):
        if start not in self._vertices:
            print(f"Node {start} does not exist.")
            return
        
        path = []
        visited = set()
        self._dfs(start, visited, path)

        return path 
    
    def _dfs(self, node, visited, path):       
        visited.add(node)
        path.append(node)

        for neighbor in self._vertices[node]:
            if neighbor.node not in visited:
                self._dfs(neighbor.node, visited, path)
        


        

if __name__ == "__main__":
    """
        A ----5-----B
        |           | \
        1           |  9
        |           |   \
        C           6    E
         \          |   /
          11        |  8
            \       | /
             F      D
    """
    g = Graph(["A", "B", "C", "D", "E", "F"])

    g.add_edge("A", "B", 5)
    g.add_edge("A", "C", 1)

    g.add_edge("B", "D", 6)
    g.add_edge("B", "E", 9)

    g.add_edge("C", "F", 11)

    g.add_edge("D", "E", 8)

    print(g)

    print("Remove E-D")
    g.remove_edge("E", "D")
    print(g)
    g.add_edge("D", "E", 8)

    print("BFS Graph Traversal: ", g.bfs("A"))

    print("DFS Graph Traversal: ", g.dfs("A"))

    print("\n\n\t EXAMPLE 2: \n\n")

    g = Graph(['a', 'b', 'c', 'd', 'e'], directed=True)      

    g.add_edge('a','b')
    g.add_edge('a','c')
    g.add_edge('a','d')
    g.add_edge('a','e')

    g.add_edge('b','d')
    g.add_edge('c','d')
    g.add_edge('c','e')
    g.add_edge('d','e')

    print(g)
    print("BFS Graph Traversal: ", g.bfs("a"))

    print("DFS Graph Traversal: ", g.dfs("a"))

    





