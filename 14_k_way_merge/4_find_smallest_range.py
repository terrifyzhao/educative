import math
from heapq import *


# 从多个数组中找到最小的范围，该范围要和所有数组有交集

def find_smallest_range(lists):
    start, end = 0, math.inf
    cur_max = -math.inf

    min_heapq = []
    for i in range(len(lists)):
        # 先把每个list中的第一个数存到heap中
        heappush(min_heapq, (lists[i][0], 0, lists[i]))
        cur_max = max(cur_max, lists[i][0])

    # heap中要和lists的个数一样多，才有计算range的意义
    while len(min_heapq) == len(lists):
        # 一直pop，最后heap中剩余的是每个list中最大的三个值
        num, i, l = heappop(min_heapq)

        # 如果有更小的范围，就更新范围
        if end - start > cur_max - num:
            start = num
            end = cur_max

        # 当前list中还有数没有被添加到heap中过，三个数的最大值减去最小值，就是范围，最小值用堆存放，最大值一直统计即可
        if len(l) > i + 1:
            heappush(min_heapq, (l[i + 1], i + 1, l))
            cur_max = max(cur_max, l[i + 1])

    return [start, end]


def main():
    print("Smallest range is: " +
          str(find_smallest_range([[1, 5], [4, 8], [7, 9]])))

    print("Smallest range is: " +
          str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()
