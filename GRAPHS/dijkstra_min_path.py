from heapq import heappop, heappush
from graphs_dict import Graph


class GraphDijkstra(Graph):

    def dijkstra(self, start, end):

        if start not in self._vertices:
            print(f"Node {start} does not exist.")
            return
        
        if end not in self._vertices:
            print(f"Node {end} does not exist.")
            return
        
        visited = set()
        unvisited = []
        heappush(unvisited, (0, start))
        distances = dict.fromkeys(self._vertices.keys(), float("inf"))

        while unvisited:
            distance, node = heappop(unvisited)

            if node == end:
                return distances[end]

            if node in visited:
                continue

            visited.add(node)

            for neighbor in self._vertices[node]:
                if neighbor.node in visited:
                    continue

                if distance + neighbor.weight < distances[neighbor.node]:
                    distances[neighbor.node] = distance + neighbor.weight
                    heappush(unvisited, (distance + neighbor.weight, neighbor.node))
    
    def dijkstra_full_graph(self, start):

        if start not in self._vertices:
            print(f"Node {start} does not exist.")
            return
    
        visited = set()
        unvisited = []
        heappush(unvisited, (0, start))

        distances = dict.fromkeys(self._vertices.keys(), float("inf"))
        distances[start] = 0
        previous_node = dict.fromkeys(self._vertices.keys())


        while unvisited:
            distance, node = heappop(unvisited)

            if node in visited:
                continue

            visited.add(node)

            for neighbor in self._vertices[node]:
                if neighbor.node in visited:
                    continue

                if distance + neighbor.weight < distances[neighbor.node]:
                    distances[neighbor.node] = distance + neighbor.weight
                    previous_node[neighbor.node] = node

                    heappush(unvisited, (distance + neighbor.weight, neighbor.node))
        
        result = {
            f"{previous_node[node]}->{node}": distances[node] for node in self._vertices
            }

        return result



if __name__ == "__main__":
    g = GraphDijkstra(["A", "B", "C", "D", "E", "F"])

    g.add_edge("A", "B", 2)
    g.add_edge("A", "D", 8)

    g.add_edge("B", "D", 5)
    g.add_edge("B", "E", 6)

    g.add_edge("D", "F", 2)
    g.add_edge("D", "E", 3)

    g.add_edge("E", "F", 1)
    g.add_edge("E", "C", 9)

    g.add_edge("F", "C", 3)

    print(g.dijkstra("A", "C"))

    print(g.dijkstra_full_graph("A"))


