from heapq import *


def find_closest_elements(arr, K, X):
    result = []
    close_index = find(arr, X)
    start = max(0, close_index - K + 1)
    end = min(close_index + K - 1, len(arr) - 1)

    for i in range(start, end + 1):
        heappush(result, (abs(arr[i] - X), arr[i]))

    res = []
    for _ in range(K):
        res.append(heappop(result)[1])
    res.sort()
    return res


def find(arr, num):
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if num < arr[mid]:
            end = mid - 1
        elif num > arr[mid]:
            start = mid + 1
        else:
            return mid
    if start >= len(arr):
        start = len(arr) - 1
    if end < 0:
        end = 0
    if num - arr[end] < arr[start] - num:
        return end
    else:
        return start


def main():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
