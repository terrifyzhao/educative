# 搜索双调数组

def search_bitonic_array(arr, key):
    start, end = 0, len(arr) - 1

    max_index = find_max_index(arr)
    index = find(arr, key, start, max_index)
    if index == -1:
        index = find(arr, key, max_index, end)
    return index


def find(arr, key, start, end):
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            return mid

        if arr[start] < arr[end]:
            if key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1

    return -1


def find_max_index(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        mid = start + (end - start) // 2

        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return start


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


main()
