import math


# 给定一个数组，找到一个最小的和大于等于s的子数组的长度

def smallest_subarray_with_given_sum(s, arr):
    length = math.inf
    sum_num = 0
    start = 0

    for end in range(len(arr)):
        sum_num += arr[end]

        while sum_num >= s:
            length = min(length, end - start + 1)
            sum_num -= arr[start]
            start += 1

    if length == math.inf:
        return 0

    return length


def smallest_subarray_with_given_sum2(s, arr):
    start = 0
    window_sum = 0
    length = 10000

    for i in range(len(arr)):
        window_sum += arr[i]
        while window_sum >= s:
            length = min(length, i - start + 1)
            window_sum -= arr[start]
            start += 1
    return 0 if length == 10000 else length


def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum2(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum2(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum2(8, [3, 4, 1, 1, 6])))


main()
