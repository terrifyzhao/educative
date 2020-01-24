def quick(nums, start, end):
    left, right = start, end
    if start < end:

        pivot = nums[left]
        while left != right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] < pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        quick(nums, start, left - 1)
        quick(nums, right + 1, end)


if __name__ == '__main__':
    nums = [23, 4, 1, 523, 2, 3, 111]
    quick(nums, 0, len(nums) - 1)
    # res = quick(nums, 5)
    print(nums)
