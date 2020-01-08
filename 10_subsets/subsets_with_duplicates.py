def find_subsets(nums):
    subsets = []

    subsets.append([])
    for num in nums:
        n = len(subsets)
        for i in range(n):
            subset = list(subsets[i])
            subset.append(num)
            if subset not in subsets:
                subsets.append(subset)

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
