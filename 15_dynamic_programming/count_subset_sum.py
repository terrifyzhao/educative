def count_subsets(num, sum):
    n = len(num)
    dp = [0 for _ in range(sum + 1)]
    dp[0] = 1

    for i in range(n):
        for j in range(sum, -1, -1):
            if j >= num[i]:
                dp[j] = dp[j] + dp[j - num[i]]

    return dp[-1]


def count_subsets2(num, sum):
    n = len(num)
    dp = [[0 for _ in range(sum + 1)] for _ in range(n)]

    for s in range(sum + 1):
        dp[0][s] = 0

    for i in range(n):
        dp[i][0] = 1

    for i in range(n):
        for j in range(sum, -1, -1):
            if j >= num[i]:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - num[i]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]


def main():
    print("Total number of subsets " + str(count_subsets2([1, 1, 2, 3], 4)))
    print("Total number of subsets " + str(count_subsets2([1, 1, 2, 3], 2)))
    print("Total number of subsets: " + str(count_subsets2([1, 2, 7, 1, 5], 9)))


main()
