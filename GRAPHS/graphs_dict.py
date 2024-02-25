"""Graph Data Structure implementation based on Python dicts."""


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
        
        self._vertices[start].append((end, weight))

        if not self._directed:
            self._vertices[end].append((start, weight))
       
    def remove_edge(self, start, end):

        if start not in self._vertices:
            print(f"Node {start} does not exist.")
            return
        
        if end not in self._vertices:
            print(f"Node {end} does not exist.")
            return
        
        remove_ind = None
        for i, (adj, _) in enumerate(self._vertices[start]):
            if adj == end:
                remove_ind = i

        if remove_ind is not None:
            self._vertices[start].pop(remove_ind)   
        else:
            print(f"Edge {start} -> {end} does not exist cannot be removed.")     

        if not self._directed:
            self.remove_edge(end, start)
        

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

    g.remove_edge("E", "D")
    print(g)




