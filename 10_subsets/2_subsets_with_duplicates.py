# 返回一个数组中的所有非重复子集

def find_subsets(nums):
    subsets = []

    subsets.append([])
    start, end = 0, 0
    for j in range(len(nums)):

        # 遇到一样的数字的时候，前面部分就不添加了，只添加后面的部分，从而避免重复
        # 后面部分的start index就是前一部分的end+1
        if j > 0 and nums[j] == nums[j - 1]:
            start = end + 1
        end = len(subsets) - 1

        for i in range(start, end + 1):
            subset = list(subsets[i])
            subset.append(nums[j])
            if subset not in subsets:
                subsets.append(subset)

    return subsets


def find_subsets(nums):
    res = []
    res.append([])
    start, end = 0, 0
    for j in range(len(nums)):

        if j > 0 and nums[j] == nums[j - 1]:
            start = end + 1
        end = len(nums) - 1
        for i in range(start, end+1):
            tmp = list(res[i])
            tmp.append(nums[i])
            res.append(tmp)
    return res


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
