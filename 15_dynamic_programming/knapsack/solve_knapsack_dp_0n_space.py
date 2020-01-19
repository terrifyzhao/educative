def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(profits) != len(weights):
        return 0

    dp = [0 for _ in range(capacity + 1)]

    # for c in range(capacity + 1):
    #     if weights[0] <= c:
    #         dp[c] = profits[0]
    for i in range(n):
        # 如果从小到大遍历，那么dp[c]的值是不是基于上一次选择的物品来的
        for c in range(capacity, -1, -1):
            if weights[i] <= c:
                dp[c] = max(dp[c], dp[c - weights[i]] + profits[i])

    return dp[-1]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
