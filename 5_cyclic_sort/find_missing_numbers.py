def find_missing_numbers(nums):
    i = 0
    n = len(nums)

    while i < n:
        # 真实下标
        j = nums[i]-1
        # 当前下标的值和真实下标的值是否一样
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    res = []
    for i in range(n):
        if nums[i] != i + 1:
            res.append(i + 1)

    return res


def main():
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers([2, 4, 1, 2]))
    print(find_missing_numbers([2, 3, 2, 1]))


main()
