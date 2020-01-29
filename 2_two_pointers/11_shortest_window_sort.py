# 给定一个数组，找到需要排序改变的最小序列长度
# tip:
# 从头找到小于前一个数的start，从后找到大于后一个数的end，从start：end中找到最大最小值，再扩大窗口，确保
# 所有的数都比最小值小，比最大值大

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


def shortest_window_sort2(arr):
    start, end = 0, len(arr) - 1

    while start < len(arr) - 1 and arr[start] <= arr[start + 1]:
        start += 1

    if start == len(arr) - 1:
        return 0

    while end > 0 and arr[end] >= arr[end - 1]:
        end -= 1

    min_num = min(arr[start:end + 1])
    max_num = max(arr[start:end + 1])

    while start > 0 and min_num < arr[start - 1]:
        start -= 1

    while end < len(arr) - 1 and max_num > arr[end + 1]:
        end += 1

    return end - start + 1


def main():
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))
    print()
    print(shortest_window_sort2([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort2([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort2([1, 2, 3]))
    print(shortest_window_sort2([3, 2, 1]))


main()
