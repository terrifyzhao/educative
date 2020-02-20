# 找到大于等于key的数

def search_ceiling_of_a_number(arr, key):
    if key > arr[-1]:
        return -1

    start, end = 0, len(arr) - 1

    while start <= end:
        mid = int(start + (end - start) / 2)

        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    # 此时start = mid+1，已经大于end了，循环结束，start指向的值刚好是大于等于key的
    return start


def search_ceiling_of_a_number(arr, key):
    if not arr:
        return -1
    if key > arr[-1]:
        return -1

    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            end = mid - 1
        else:
            start = mid+1

    return start


def main():
    # print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
