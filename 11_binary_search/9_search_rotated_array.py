# 搜索旋转数组

def search_rotated_array(arr, key):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            return mid

        # mid左边是升序的
        if arr[start] <= arr[mid]:

            if arr[start] <= key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        else:
            if arr[mid] < key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1


def search_rotated_array2(arr, key):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            return mid

        if arr[start] <= arr[mid]:
            if arr[start] <= key < arr[mid]:
                end = mid - 1
            else:
                start = mid
        else:
            if arr[mid] < key <= arr[end]:
                start = mid + 1
            else:
                end = mid
    return -1


def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))


main()
