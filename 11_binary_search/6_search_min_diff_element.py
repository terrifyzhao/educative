# 找到和key相差最小的数

def search_min_diff_element(arr, key):
    if key < arr[0]:
        return arr[0]
    if key > arr[-1]:
        return arr[-1]

    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            return arr[mid]

    if arr[start] - key <= abs(key - arr[end]):
        return arr[start]
    else:
        return arr[end]


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


main()
