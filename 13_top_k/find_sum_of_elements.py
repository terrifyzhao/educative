from heapq import *


def find_sum_of_elements(nums, k1, k2):
    min_heap = []
    for num in nums:
        heappush(min_heap, num)

    i = 1
    while i <= k1:
        heappop(min_heap)
        i += 1

    res = 0
    while i < k2:
        res += heappop(min_heap)
        i += 1
    return res


def main():
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()
