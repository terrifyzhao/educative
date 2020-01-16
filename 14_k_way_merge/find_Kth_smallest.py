from heapq import *


def find_Kth_smallest(lists, k):
    min_heap = []
    for i in range(len(lists)):
        heappush(min_heap, (lists[i][0], 0, lists[i]))

    count = 0
    num = 0
    while min_heap:
        num, i, l = heappop(min_heap)
        count += 1
        if count == k:
            return num

        # 如果当前值的list中还有多余的值，就添加到堆中
        if len(l) > i + 1:
            heappush(min_heap, (l[i + 1], i + 1, l))

    return num


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()
