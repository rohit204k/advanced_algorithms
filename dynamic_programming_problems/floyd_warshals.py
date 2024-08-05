from graph import Graph as G


def floyd_warshal(g: G):
    n = len(g.v)
    dp = [[[0 for i in range(n)] for j in range(n)] for _ in range(n)]

    dp[0] = [
        [
            g.adjacency_matrix[i][j] if g.adjacency_matrix[i][j] != 0 else float("inf")
            for j in range(n)
        ]
        for i in range(n)
    ]
    for i in range(n):
        dp[0][i][i] = 0

    for k in range(1, n):
        for i in range(n):
            for j in range(n):
                dp[k][i][j] = min(dp[k - 1][i][j], dp[k - 1][i][k] + dp[k - 1][k][j])

    return dp[n - 1]


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


def main():
    vertices = [1, 2, 3, 4, 5]
    edges = [
        (1, 2),
        (1, 4),
        (2, 3),
        (2, 5),
        (3, 1),
        (3, 4),
        (4, 3),
        (4, 5),
        (5, 1),
        (5, 4),
    ]
    weights = [4, 5, 1, 6, 2, 3, 1, 2, 1, 4]

    g = G(vertices, edges, weights, directed=True)

    print("Graph adjacency matrix: \n")
    print(g)

    min_distance = floyd_warshal(g)

    print(
        "\nFinding shortest distance between all pairs of vertices using Floyd-Warshals Algorithm\n"
    )

    min_distance = format_matrix(min_distance, g)

    print(min_distance)

    # print('Minimum Distance between each pair of vertices\n')
    # for row in min_distance:
    #     print(row,'\n')


if __name__ == "__main__":
    main()
