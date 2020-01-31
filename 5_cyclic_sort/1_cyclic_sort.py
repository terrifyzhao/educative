# 数组的数包含1-n，对其排序

def cyclic_sort(nums):
    i = 0

    while i < len(nums):
        # 正确的下标
        j = nums[i] - 1
        # 当前值和正确下标的值不同
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    return nums


def cyclic_sort2(nums):
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()
