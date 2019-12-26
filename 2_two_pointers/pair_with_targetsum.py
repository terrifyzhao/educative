def pair_with_targetsum(arr, target_sum):
    arr_len = len(arr)
    start = 0
    end = arr_len - 1
    while start < end:
        if arr[start] + arr[end] > target_sum:
            end -= 1
        elif arr[start] + arr[end] < target_sum:
            start += 1
        elif arr[start] + arr[end] == target_sum:
            break
    return [start, end]


def pair_with_targetsum2(arr, target_sum):
    dic = {}

    for i, num in enumerate(arr):
        if target_sum - num in dic:
            return [dic[target_sum - num], i]
        else:
            dic[num] = i
    return [-1, -1]
