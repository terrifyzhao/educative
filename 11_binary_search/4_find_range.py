# 找key出现在arr中的范围


def find_range(arr, key):
    result = [- 1, -1]
    result[0] = find(arr, key, True)
    if result[0] != -1:
        result[1] = find(arr, key, False)
    return result


def find(arr, key, find_start):
    start, end = 0, len(arr) - 1
    key_index = -1
    while start <= end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            key_index = mid
            if find_start:
                end = mid - 1
            else:
                start = mid + 1
    return key_index


def find(arr, key, find_start):
    index = -1
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            index = mid
            if find_start:
                end = mid - 1
            else:
                start = mid + 1
    return index


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
