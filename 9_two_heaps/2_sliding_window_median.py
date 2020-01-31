from heapq import *
import heapq


class SlidingWindowMedian:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def find_sliding_window_median(self, nums, k):
        result = []
        for i in range(len(nums)):
            if not self.max_heap or -self.max_heap[0] >= nums[i]:
                heappush(self.max_heap, -nums[i])
            else:
                heappush(self.min_heap, nums[i])

            self.rebalance()

            # 已经有k个元素了
            if i - k + 1 >= 0:
                if len(self.max_heap) == len(self.min_heap):
                    result.append((-self.max_heap[0] + self.min_heap[0]) / 2)
                else:
                    result.append(-self.max_heap[0])

                # 划窗第一个元素
                remove_element = nums[i - k + 1]

                if remove_element <= -self.max_heap[0]:
                    self.remove(self.max_heap, -remove_element)
                else:
                    self.remove(self.min_heap, remove_element)

                self.rebalance()
        return result

    def rebalance(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def remove(self, heap, num):
        idx = heap.index(num)
        heap[idx] = heap[-1]
        heap.pop()

        if idx < len(heap):
            heapq._siftup(heap, idx)
            heapq._siftdown(heap, 0, idx)
            # heapq.heapify(heap)


class SlidingWindowMedian:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def find_sliding_window_median(self, nums, k):
        result = []

        for i in range(len(nums)):

            if not self.max_heap or nums[i] <= -self.max_heap[0]:
                heappush(self.max_heap, -nums[i])
            else:
                heappush(self.min_heap, nums[i])

            self.balance()

            if i >= k - 1:
                if len(self.max_heap) == len(self.min_heap):
                    result.append((-self.max_heap[0] + self.min_heap[0]) / 2)
                else:
                    result.append(-self.max_heap[0])

                element = nums[i - k + 1]
                if element <= -self.max_heap[0]:
                    self.remove(self.max_heap, -element)
                else:
                    self.remove(self.min_heap, element)
                self.balance()

        return result

    def balance(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))

        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def remove(self, heap, num):
        idx = heap.index(num)
        heap[idx] = heap[-1]
        heap.pop()

        if idx < len(heap):
            heapq._siftup(heap, idx)
            heapq._siftdown(heap, 0, idx)


def main():
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
