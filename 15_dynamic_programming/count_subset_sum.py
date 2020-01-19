def count_subsets(num, sum):
    n = len(num)
    dp = [0 for _ in range(sum + 1)]
    dp[0] = 1

    for i in range(n):
        for j in range(sum, -1, -1):
            dp[j]


    return -1


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
