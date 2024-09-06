from collections import deque, defaultdict

class Graph:
    '''
    Graph Class
    vertices: list of vertices (vertices are numbered from 1 and onwards.)
    edges: list of edges (each edge is a tuple of form (s,v), ex: (1,2))
    weights: list of weights in order pass in edges, defaults to None, which is 1 for all edges
    directed: True for directed graphs, False otherwise.
    '''
    def __init__(self, vertices, edges, weights=None, directed=False) -> None:
        self.v = vertices
        self.e = {}
        if weights is None:
            weights = [1] * len(edges)

        for i in range(len(edges)):
            self.e[edges[i]] = weights[i]

        self.adjacency_matrix = [[0] * len(self.v) for _ in range(len(self.v))]

        for (u, v), weight in self.e.items():
            self.adjacency_matrix[u - 1][v - 1] = weight
            if not directed:
                self.adjacency_matrix[v - 1][u - 1] = weight

    def format_matrix_row(self, array, width = 3):
        return [
            f"{'inf' if val == float('inf') else int(val):>{width}}" for val in array
        ]

    def __str__(self):

        matrix_str = "  " + " ".join(map(str, self.format_matrix_row(self.v))) + "\n"

        for i in range(len(self.v)):
            matrix_str += (
                str(self.v[i])
                + " "
                + " ".join(map(str, self.format_matrix_row(self.adjacency_matrix[i])))
                + "\n"
            )

        return matrix_str

## Write Usage
class BipartiteGraph:
    def __init__(self, U, V, edges, weights=None) -> None:
        self.U = U
        self.V = V
        self.e = {}
        if weights is None:
            weights = [1] * len(edges)

        for i in range(len(edges)):
            self.e[edges[i]] = weights[i]

        self.adjacency_matrix = self.create_adjacency_matrix()
        self.adjacency_list = self.create_adjacency_list()

    def update_edge_parameters(self):
        self.adjacency_matrix = self.create_adjacency_matrix()
        self.adjacency_list = self.create_adjacency_list()

    def create_adjacency_matrix(self):
        # Initialize the adjacency matrix with zeros
        matrix = [[0] * len(self.V) for _ in range(len(self.U))]

        # Fill the adjacency matrix with weights
        for (u, v), weight in self.e.items():
            u_index = self.U.index(u)
            v_index = self.V.index(v)
            matrix[u_index][v_index] = weight

        return matrix

    def create_adjacency_list(self):
        adj_list = defaultdict(list)
        for (u, v), _ in self.e.items():
            adj_list[u].append(v)
            # adj_list[v].append(u)  # if the graph is undirected
        return adj_list
    
    def __str__(self):
        matrix_str = "  " + " ".join(map(str, self.V)) + "\n"

        for i, row in enumerate(self.adjacency_matrix):
            matrix_str += str(self.U[i]) + " " + " ".join(map(str, row)) + "\n"

        return matrix_str


class MultiGraph:
    '''
    The MultiGraph class is implemented specifically to solve the Karger's min cut problem. It is undirected unweighted graph with multiple edges
    between any pair of vertices.
    '''
    def __init__(self, vertices, edges, weights=None, directed=False) -> None:
        self.v = vertices
        self.e = {}

        # if weights is None:
        #     weights = [1] * len(edges)

        for i in range(len(edges)):
            # self.e[edges[i]] += weights[i]
            self.e[edges[i]] = self.e.get(edges[i], 0) + 1

        self.adjacency_matrix = [[0] * len(self.v) for _ in range(len(self.v))]

        for (u, v), weight in self.e.items():
            self.adjacency_matrix[u - 1][v - 1] = weight
            if not directed:
                self.adjacency_matrix[v - 1][u - 1] = weight

    def format_matrix_row(self, array, width = 3):
        return [
            f"{'inf' if val == float('inf') else int(val):>{width}}" for val in array
        ]

    def __str__(self):

        matrix_str = "  " + " ".join(map(str, self.format_matrix_row(self.v))) + "\n"

        for i in range(len(self.v)):
            matrix_str += (
                str(self.v[i])
                + " "
                + " ".join(map(str, self.format_matrix_row(self.adjacency_matrix[i])))
                + "\n"
            )

        return matrix_str