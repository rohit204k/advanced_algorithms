import numpy as np
from graph import Graph as G


def format_matrix(array, g: G):

    def format_array(array, width=3):
        return [
            f"{'inf' if val == float('inf') else int(val):>{width}}" for val in array
        ]

    matrix_str = "  " + " ".join(map(str, format_array(g.v))) + "\n"

    for i in range(len(g.v)):
        matrix_str += (
            str(g.v[i]) + " " + " ".join(map(str, format_array(array[i]))) + "\n"
        )

    return matrix_str


def matrix_multiplication(A, B):
    """Performs matrix multiplication of two 2D matrices

    Args:
        A (2D array): Matrix A
        B (2D array): Matrix B

    Returns:
        2D array: Matrix product of A and B
    """
    A = np.array(A)
    B = np.array(B)

    n = A.shape[0]

    C = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i, j] += A[i, k] * B[k, j]

    return C


def calculate_G2(g: G):
    vertices_g2 = g.v.copy()

    square_adj_matrix = matrix_multiplication(g.adjacency_matrix, g.adjacency_matrix)
    edges_g2 = [
        (i, j)
        for i in vertices_g2
        for j in vertices_g2
        if (
            (
                g.adjacency_matrix[i - 1][j - 1] == 1
                or (square_adj_matrix[i - 1][j - 1] > 0)
            )
            and i < j
        )
    ]

    return G(vertices_g2, edges_g2)

def check_diagonals(g: G) -> G:
    """Checks if all the non-diagonal elements of adjacency matrix of `g` are 1. If yes, return True and False otherwise.

    Args:
        g (G): Graph
    """

    for i in g.v:
        for j in g.v:
            if i != j and g.adjacency_matrix[i - 1][j - 1] != 1:
                return False
    
    return True

def compute_degree(M_g, j: int) -> int:
    """Returns the number of edges incident to node j in graph G.

    Args:
        M_g (2D array): Adjacency Matrix of graph G
        j (int): Node

    Returns:
        int: Number of nodes
    """
    return M_g[j].count(1)

def compute_parity(D_g2, M_g):
    X = matrix_multiplication(D_g2, M_g)
    
    P_g = np.zeros((len(X), len(X[0])))

    for i in range(len(M_g)):
        for j in range(len(M_g[0])):
            if (X[i, j]/compute_degree(M_g, j)) < D_g2[i][j]:
                P_g[i, j] = 1

    return P_g

def seidels(g: G):
    g2 = calculate_G2(g)
    
    D_g = [[0 for _ in g.v] for _ in g.v]

    if check_diagonals(g2):

        for i in g.v:
            for j in g.v:
                if i == j:
                    D_g[i - 1][j - 1] = 0
                elif g.adjacency_matrix[i - 1][j - 1] == 1:
                    D_g[i - 1][j - 1] = 1
                else:
                    D_g[i - 1][j - 1] = 2
    else:
        D_g2 = seidels(g2)
        P_g = compute_parity(D_g2, g.adjacency_matrix)
        for i in g.v:
            for j in g.v:
                D_g[i - 1][j - 1] = int((2 * D_g2[i - 1][j - 1]) - P_g[i - 1][j - 1])
        
    return D_g

def main():
    vertices = [1, 2, 3, 4, 5]
    edges = [(1, 2), (2, 3), (3, 4), (4, 5)]

    g = G(vertices, edges)

    print('Graph adjacency matrix: \n')
    print(g)

    D_g = seidels(g)

    print('\nFinding distance between all pairs of vertices using Seidel\'s Algorithm\n')    
    
    distance = format_matrix(D_g, g)
    print(distance)

if __name__ == "__main__":
    main()
