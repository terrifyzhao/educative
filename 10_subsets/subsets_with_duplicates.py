def find_subsets(nums):
    subsets = []

    subsets.append([])
    start, end = 0, 0
    for j in range(len(nums)):

        if j > 0 and nums[j] == nums[j - 1]:
            start = end + 1
        end = len(subsets) - 1

        for i in range(start, end + 1):
            subset = list(subsets[i])
            subset.append(nums[j])
            if subset not in subsets:
                subsets.append(subset)

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
