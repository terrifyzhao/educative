def max_sub_array_of_size_k(k, arr):
    if not arr:
        return None

    max_num = 0
    tmp_sum = 0
    window_start = 0
    for end in range(len(arr)):
        tmp_sum += arr[end]
        if end + 1 >= k:
            max_num = max(max_num, tmp_sum)
            tmp_sum -= arr[window_start]
            window_start += 1
    return max_num


def max_sub_array_of_size_k2(k, nums):
    window_sum = 0
    start = 0
    max_sum = 0

    for i in range(len(nums)):
        window_sum += nums[i]
        if i >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[start]
            start += 1
    return max_sum


def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k2(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k2(2, [2, 3, 4, 1, 5])))


main()
