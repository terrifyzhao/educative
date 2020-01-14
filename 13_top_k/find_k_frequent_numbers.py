from heapq import *


def find_k_frequent_numbers(nums, k):
    topNumbers = []

    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1

    for num, fre in dic.items():
        heappush(topNumbers, (fre, num))
        if len(topNumbers) > k:
            heappop(topNumbers)

    res = []
    while topNumbers:
        res.append(heappop(topNumbers)[1])

    return res


def main():
    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()
