# 返回一个数组中的所有子集

def find_subsets(nums):
    subsets = []
    subsets.append([])

    for num in nums:
        n = len(subsets)
        for i in range(n):
            subset = list(subsets[i])
            subset.append(num)
            subsets.append(subset)

    return subsets


def find_subsets(nums):
    res = []
    res.append([])

    for num in nums:
        n = len(res)
        for i in range(n):
            tmp = list(res[i])
            tmp.append(num)
            res.append(tmp)
    return res

def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
