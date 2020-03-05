from heapq import *


# 移除k个元素，剩余最多的不同元素个数

def find_maximum_distinct_elements(nums, k):
    dic = {}

    for num in nums:
        dic[num] = dic.get(num, 0) + 1

    res = 0
    min_heap = []
    for num, fre in dic.items():
        if fre == 1:
            res += 1
        else:
            heappush(min_heap, (fre, num))

    while k > 0 and min_heap:
        k -= min_heap.pop()[0] - 1
        if k >= 0:
            res += 1

    if k > 0:
        res -= k

    return res


def main():
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers after removing K numbers: " +
          str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()
