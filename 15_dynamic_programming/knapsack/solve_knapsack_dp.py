def solve_knapsack(profits, weights, capacity):
    # 1、确定dp数组 dp[i][j]表示的是取i个item，capacity为j时的收益
    dp = [[0 for _ in range(capacity + 1)] for _ in range(len(profits))]

    # 2、初始化dp数组
    for i in range(len(profits)):
        # capacity是0所以对应的收益全是0
        dp[i][0] = 0

    for c in range(capacity + 1):
        # 权重小于等于c才能加到包里, i是从0开始的，所以0表示第一个item
        if weights[0] <= c:
            dp[0][c] = profits[0]

    # 3、确定状态转移方程
    for i in range(len(profits)):
        for c in range(capacity + 1):
            pro1, pro2 = 0, 0
            if weights[i] <= c:
                pro1 = profits[i] + dp[i - 1][c - weights[i]]
            pro2 = dp[i - 1][c]
            dp[i][c] = max(pro1, pro2)

    return dp[-1][-1]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
