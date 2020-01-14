from heapq import *


def find_k_largest_numbers(nums, k):
    result = []

    for i in range(k):
        heappush(result, nums[i])

    for num in nums[k:]:
        if num > result[0]:
            heappop(result)
            heappush(result, num)

    return result


def main():
    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()
