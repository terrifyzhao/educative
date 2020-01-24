def find_Kth_smallest_number(nums, k):
    return find_Kth_smallest_number_rec(nums, k, 0, len(nums) - 1)


def find_Kth_smallest_number_rec(nums, k, start, end):
    p = partition(nums, start, end)

    if p == k - 1:
        return nums[p]
    if p > k - 1:
        return find_Kth_smallest_number_rec(nums, k, start, p - 1)
    return find_Kth_smallest_number_rec(nums, k, p + 1, end)


def partition(nums, left, right):
    pivot = nums[left]

    while left != right:
        while left < right and nums[right] >= pivot:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] < pivot:
            left += 1
        nums[right] = nums[left]
    nums[left] = pivot
    return left


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

    # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()
