# 数组的数包含1-n，找到重复的

def find_duplicate(nums):
    i = 0
    n = len(nums)

    while i < n:
        # 当前下标的值不对
        if nums[i] != i + 1:
            j = nums[i] - 1
            # 当前下标的值和真实下标的值不对
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i]
        else:
            i += 1

    return -1


def find_duplicate2(nums):
    i = 0

    while i < len(nums):
        if nums[i] != i + 1:
            j = nums[i] - 1

            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i]
        else:
            i += 1

    return -1


def main():
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 4, 1, 4, 4]))


main()
