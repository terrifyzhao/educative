def can_partition(num):
    n = len(num)
    s = sum(num) // 2
    # dp[i][s]表示的是从0到i个元素中选一些数，能否使其和为s
    dp = [[False for _ in range(s + 1)] for _ in range(n)]

    # 加和为0的，不管有几个数都设置为True
    for i in range(n):
        dp[i][0] = True

    # 1个数值的时候，判断该数值和s是否相等
    for j in range(s + 1):
        dp[0][j] = num[0] == j

    for i in range(n):
        for j in range(1, s + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i - 1][j - num[i]]

    return dp[n - 1][s]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
