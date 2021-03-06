# num的子集是否和等于sum

def can_partition(num, sum):
    dp = [False for _ in range(sum + 1)]
    dp[0] = True

    for s in range(1, sum + 1):
        dp[s] = s == num[0]

    for i in range(1, len(num)):
        for s in range(sum, -1, -1):
            if not dp[s] and s >= num[i]:
                dp[s] = dp[s - num[i]]

    return dp[sum]


def can_partition2(num, sum):
    dp = [False for _ in range(sum + 1)]
    dp[0] = True

    # for s in range(sum + 1):
    #     dp[s] = s == num[0]

    for i in range(len(num)):
        for s in range(sum, -1, -1):
            if not dp[s] and s >= num[i]:
                dp[s] = dp[s - num[i]]

    return dp[-1]


def main():
    print("Can partition: " + str(can_partition2([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition2([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition2([1, 3, 4, 8], 6)))


main()
