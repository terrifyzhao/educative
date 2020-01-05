def find_first_k_missing_positive(nums, k):
    missingNumbers = []

    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1

        if 0 < nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    extra_num = set()
    for i in range(n):
        if nums[i] != i + 1 and len(missingNumbers) < k:
            missingNumbers.append(i + 1)
            extra_num.add(nums[i])
    i = 1
    while len(missingNumbers) < k:
        if n + i not in extra_num:
            missingNumbers.append(n + i)
        i += 1

    return missingNumbers


def main():
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))


main()
