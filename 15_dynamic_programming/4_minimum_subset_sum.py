# 计算num两个子集的最小差

def can_partition(num):
    s = sum(num)
    n = len(num)

    s //= 2

    dp = [False for _ in range(s + 1)]

    dp[0] = True

    for i in range(n):
        for j in range(s, -1, - 1):
            if not dp[j] and j >= num[i]:
                dp[j] = dp[j - num[i]]

    num1 = 0
    for j in range(s, -1, - 1):
        if dp[j]:
            num1 = j
            break

    num2 = sum(num) - num1
    return abs(num2 - num1)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()
