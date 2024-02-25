"""
Module implementing Graphs Data Structure
"""


class Graph:
    """
    Weighted Graph implementation using mathematical concept of
    adjacency matrix via python lists.
    """

    def __init__(self, vertices: list, directed: bool = False, default_weight=None):
        self.matrix_len = len(vertices)
        self.vertices = vertices
        self.directed = directed
        self.default_weight = default_weight

        self.matrix = None
        self.init_matrix()

    def __str__(self) -> str:

        message = "\n".join(
            [
                "  ".join([*[str(elem) for elem in row], str(vx)])
                for vx, row in zip(self.vertices, self.matrix)
            ]
        )

        return "\n" + message + "\n"

    def init_matrix(self):
        self.matrix = [
            [self.default_weight for _ in range(self.matrix_len)]
            for _ in range(self.matrix_len)
        ]

    def get_vertices_indexes(self, start, end):
        start_ind = self.vertices.index(start)
        end_ind = self.vertices.index(end)

        return start_ind, end_ind

    def add_edge(self, start, end, weight=1) -> None:
        start_ind, end_ind = self.get_vertices_indexes(start, end)

        self.matrix[start_ind][end_ind] = weight

        if not self.directed:
            self.matrix[end_ind][start_ind] = weight

    def contains_edge(self, start, end):
        start_ind, end_ind = self.get_vertices_indexes(start, end)
        weight = self.matrix[start_ind][end_ind]

        if weight == self.default_weight:
            print(f"Edge from {start} to {end} doesn't exist.")

        return weight

    def remove_edge(self, start, end) -> None:
        start_ind, end_ind = self.get_vertices_indexes(start, end)
        weight = self.matrix[start_ind][end_ind]

        if weight == self.default_weight:
            print(f"Edge from {start} to {end} doesn't exist cannot remove.")

        self.matrix[start_ind][end_ind] = self.default_weight


if __name__ == "__main__":
    g = Graph(["A", "B", "C", "D"], default_weight=0)
    print(g)
    
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("D", "B")
    print(g)
