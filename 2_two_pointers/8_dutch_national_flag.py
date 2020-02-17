# 对只包含0 1 2 的数组排序

def dutch_flag_sort(arr):
    start = 0
    end = len(arr) - 1

    i = 0
    while i <= end:
        if arr[i] == 0:
            arr[start], arr[i] = arr[i], arr[start]
            i += 1
            start += 1
        elif arr[i] == 1:
            i += 1
        elif arr[i] == 2:
            arr[end], arr[i] = arr[i], arr[end]
            # 这里不需要i+1，因为i替换后可能为0、1、2，而arr[i]==0的时候是从左往右遍历的，只可能存在0
            # i += 1
            end -= 1

    return arr


def main():
    arr = [1, 0, 2, 1, 0]
    dutch_flag_sort(arr)
    print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(arr)
    print(arr)


main()
