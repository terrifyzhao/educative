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
