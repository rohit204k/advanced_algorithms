def knapsack(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(capacity + 1):
            if j >= items[i - 1]:
                dp[i][j] = max(dp[i - 1][j], items[i - 1] + dp[i - 1][j - items[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    c = capacity

    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][c] == dp[i - 1][c]:
            selected_items.append(items[i - 1])
            c -= items[i - 1]
    return dp[n][capacity], selected_items



def main():
    print("Dynamic Programming - Knapsack")
    items = [7, 5, 4]
    print(f"Items = {items}")

    capacity = 10
    print(f"Capacity = {capacity}\n")

    optimal_weight, selected_items = knapsack(items, capacity)

    print(f"Optimal Weight = {optimal_weight}")
    print(f"Selected Items = {selected_items}")


if __name__ == "__main__":
    main()
