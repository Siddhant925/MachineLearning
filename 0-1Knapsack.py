def knapsack(weights, profits, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Fill the table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


n = int(input("Enter number of items: "))

weights = []
profits = []

for i in range(n):
    weights.append(int(input(f"Enter weight of item {i + 1}: ")))
    profits.append(int(input(f"Enter profit of item {i + 1}: ")))

capacity = int(input("Enter knapsack capacity: "))

print("Maximum Profit:", knapsack(weights, profits, capacity))
