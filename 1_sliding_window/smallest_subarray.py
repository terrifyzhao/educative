import math


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

print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))