from __future__ import print_function
from heapq import *


def find_k_largest_pairs(nums1, nums2, k):
    min_heap = []

    for i in range(min(len(nums1), k)):
        for j in range(min(len(nums2), k)):
            # 不够k就加和的值push到堆中
            if len(min_heap) < k:
                heappush(min_heap, (nums1[i] + nums2[j], i, j))
            else:
                # 如果k够了，加和的值大于堆顶的值，则pop出堆顶的值，并加入新的加和值
                if nums1[i] + nums2[j] < min_heap[0][0]:
                    break
                else:
                    heappop(min_heap)
                    heappush(min_heap, (nums1[i] + nums2[j], i, j))
                    
    # 最后堆里剩余的是最大的三个加和的值
    res = []
    while min_heap:
        _, i, j = heappop(min_heap)
        res.append([nums1[i], nums2[j]])

    return res


def main():
    print("Pairs with largest sum are: " +
          str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()
