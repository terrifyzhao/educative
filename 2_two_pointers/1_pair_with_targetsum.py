# 给定一个数组，找到相加等于sum的数的下标


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


def pair_with_targetsum3(arr, target_sum):
    dic = {}

    for index, num in enumerate(arr):
        if target_sum - num in dic:
            return [index, dic[target_sum - num]]
        else:
            dic[num] = index
    return [-1, -1]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))

    print(pair_with_targetsum2([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum2([2, 5, 9, 11], 11))

    print(pair_with_targetsum3([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum3([2, 5, 9, 11], 11))


main()
