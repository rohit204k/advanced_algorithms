from bipartite_graph import BipartiteGraph as BG
from collections import deque

NIL = None


def maximum_matching(graph: BG):
    U, V = graph.U, graph.V
    adj = graph.adjacency_list
    pair_U = {u: NIL for u in U}
    pair_V = {v: NIL for v in V}
    dist = {}

    def bfs():
        queue = deque()
        for u in U:
            if pair_U[u] == NIL:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[NIL] = float('inf')

        while queue:
            u = queue.popleft()
            if dist[u] < dist[NIL]:
                for v in adj[u]:
                    if dist[pair_V[v]] == float('inf'):
                        dist[pair_V[v]] = dist[u] + 1
                        queue.append(pair_V[v])
        return dist[NIL] != float('inf')

    def dfs(u):
        if u != NIL:
            for v in adj[u]:
                if dist[pair_V[v]] == dist[u] + 1:
                    if dfs(pair_V[v]):
                        pair_V[v] = u
                        pair_U[u] = v
                        return True
            dist[u] = float('inf')
            return False
        return True

    matching_size = 0
    while bfs():
        for u in U:
            if pair_U[u] == NIL and dfs(u):
                matching_size += 1

    return matching_size, pair_U, pair_V


def main():
    U = [1, 2, 3, 4]
    V = [5, 6, 7]
    # edges = [(1, 5), (1, 6), (2, 6), (2, 7), (3, 7), (4, 7), (4, 8)]
    edges = [(1, 5), (2, 5), (3, 6), (3, 7), (4, 6)]

    g = BG(U, V, edges)

    print("\nFinding Maximum Matching for a Bipartite Graph\n")

    print("Graph adjacency matrix: \n")
    print(g)
    
    matching_size, pair_U, pair_V = maximum_matching(g)
    
    print(f"\nMaximum matching size: {matching_size}")
    print(f"Matching pairs from U to V: {pair_U}")
    print(f"Matching pairs from V to U: {pair_V}")

if __name__ == "__main__":
    main()
