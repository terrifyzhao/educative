def length_of_longest_substring(arr, k):
    max_len = 0
    start = 0
    num_sum = 0
    for end in range(len(arr)):
        num_sum += arr[end]

        if end - start + 1 - num_sum > k:
            num_sum -= arr[start]
            start += 1

        max_len = max(max_len, end - start + 1)

    return max_len
