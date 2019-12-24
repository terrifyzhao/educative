def slid(arr, k):
    res = []
    window_sum = 0
    window_start = 0
    for end in range(len(arr)):
        window_sum += arr[end]
        if end + 1 >= k:
            res.append(window_sum / k)
            window_sum -= arr[window_start]
            window_start += 1

    return res


print(slid([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
