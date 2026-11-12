def fractional_knapsack(capacity, weights, profits):
    n = len(weights)

    # Calculate profit-to-weight ratio
    items = []
    for i in range(n):
        ratio = profits[i] / weights[i]
        items.append((ratio, weights[i], profits[i]))

    # Sort items by ratio in descending order
    items.sort(reverse=True)

    total_profit = 0

    for ratio, weight, profit in items:
        if capacity >= weight:
            # Take the complete item
            capacity -= weight
            total_profit += profit
        else:
            # Take the fraction of the item
            total_profit += ratio * capacity
            break

    return total_profit


n = int(input("Enter number of items: "))

weights = []
profits = []

for i in range(n):
    w = float(input(f"Enter weight of item {i+1}: "))
    p = float(input(f"Enter profit of item {i+1}: "))
    weights.append(w)
    profits.append(p)

capacity = float(input("Enter knapsack capacity: "))

max_profit = fractional_knapsack(capacity, weights, profits)

print("Maximum Profit:", max_profit)
