# 数组的数包含0-n，找到缺失的

def find_missing_number(nums):
    i = 0
    n = len(nums)

    while i < n:
        j = nums[i]

        # 不能是和长度一样的值，是该值就不移动，因为没有多余的空间存储该值，最后该值的位置就是缺失值的位置
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if i != nums[i]:
            return i

    return n


def find_missing_number2(nums):
    i = 0

    while i < len(nums):
        j = nums[i]
        # 注意处理最大的数
        if nums[i] != i and j != len(nums):
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i, n in enumerate(nums):
        if n != i:
            return i


def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()
