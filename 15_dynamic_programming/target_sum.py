def find_target_subsets(num, s):
    total_sum = sum(num)

    if total_sum < s or (total_sum + s) & 1 == 1:
        return 0

    return f(num, (total_sum + s) // 2)


def f(num, s):
    n = len(num)
    dp = [0 for _ in range(s + 1)]

    dp[0] = 1

    for i in range(n):
        for j in range(s, -1, -1):
            if j >= num[i]:
                dp[j] = dp[j] + dp[j - num[i]]

    return dp[-1]


def main():
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()
