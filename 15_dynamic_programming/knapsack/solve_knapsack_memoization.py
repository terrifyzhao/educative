def knapsack(dp, profits, weights, capacity, cur_index):
    if capacity <= 0 or cur_index >= len(profits):
        return 0

    if dp[cur_index][capacity] != -1:
        return dp[cur_index][capacity]

    # 每次有两种情况，选或者不选
    # 选的情况
    profit1 = 0
    if weights[cur_index] <= capacity:
        profit1 = profits[cur_index] + \
                  knapsack(dp, profits, weights, capacity - weights[cur_index], cur_index + 1)

    # 不选的情况
    profit2 = knapsack(dp, profits, weights, capacity, cur_index + 1)

    dp[cur_index][capacity] = max(profit1, profit2)
    return dp[cur_index][capacity]


def solve_knapsack(profits, weights, capacity):
    # dp[i][capacity]表示的是第i个item对应capacity的最大收益
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(len(profits))]
    return knapsack(dp, profits, weights, capacity, 0)


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
