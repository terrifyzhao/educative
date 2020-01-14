from heapq import *


class KthLargestNumberInStream:
    def __init__(self, nums, k):
        self.k = k
        self.res = []
        for num in nums:
            heappush(self.res, num)

    def add(self, num):
        heappush(self.res, num)
        while len(self.res) > self.k:
            heappop(self.res)

        return self.res[0]


def main():
    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()
