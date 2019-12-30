def shortest_window_sort(arr):
    low, high = 0, len(arr) - 1

    while low < len(arr) - 1 and arr[low] <= arr[low + 1]:
        low += 1

    if low == len(arr) - 1:
        return 0

    while high > 0 and arr[high] >= arr[high - 1]:
        high -= 1

    min_num = min(arr[low:high + 1])
    max_num = max(arr[low:high + 1])

    while low > 0 and min_num < arr[low - 1]:
        low -= 1

    while high < len(arr) - 1 and max_num > arr[high + 1]:
        high += 1

    return high - low + 1
