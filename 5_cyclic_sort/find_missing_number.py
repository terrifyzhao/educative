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


def main():
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()
