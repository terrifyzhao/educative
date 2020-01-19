def can_partition(num):
    n = len(num)
    s = sum(num)
    if s & 1 == 1:
        return False
    s //= s

    # dp[i][s]表示的是从0到i个元素中选一些数，能否使其和为s
    dp = [[False for _ in range(s + 1)] for _ in range(n)]

    # 加和为0的，不管有几个数都设置为True，因为其中一个子集可以为空
    for i in range(n):
        dp[i][0] = True

    # 1个数值的时候，判断该数值和s是否相等
    # for j in range(s + 1):
    #     dp[0][j] = num[0] == j
    dp[0][num[0]] = True

    for i in range(n):
        for j in range(1, s + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i - 1][j - num[i]]

    return dp[n - 1][s]


def f(num):
    s = sum(num)
    if s & 1 == 1:
        return False
    s //= 2

    dp = [False for _ in range(s + 1)]
    dp[0] = True

    if num[0] == s:
        dp[num[0]] = True

    for i in range(1, len(num)):
        for j in range(s, -1, -1):
            if not dp[j] and j >= num[i]:

                dp[j] = dp[j - num[i]]

    return dp[-1]


def main():
    print("Can partition: " + str(f([1, 2, 3, 4])))
    print("Can partition: " + str(f([1, 1, 3, 4, 7])))
    print("Can partition: " + str(f([2, 3, 4, 6])))


main()
