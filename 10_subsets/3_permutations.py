from collections import deque


# 数组的排列组合
def find_permutations(nums):
    result = []
    nums_len = len(nums)
    permutation = deque()
    permutation.append([])
    for num in nums:

        # 这一层的遍历是遍历所有的permutations
        while permutation:
            old_permutation = permutation.popleft()
            # 这一层是遍历所有的位置
            # 创建一个新的permutation，在每个位置都插入num
            for j in range(len(old_permutation) + 1):
                new_permutation = list(old_permutation)
                new_permutation.insert(j, num)
                if len(new_permutation) == nums_len:
                    result.append(new_permutation)
                else:
                    permutation.append(new_permutation)
    return result


def find_permutations(nums):
    n = len(nums)
    res = []
    permutations = deque()
    permutations.append([])

    for num in nums:

        for _ in range(len(permutations)):

            old_permutation = permutations.popleft()

            for j in range(len(old_permutation) + 1):
                permutation = list(old_permutation)
                permutation.insert(j, num)

                if len(permutation) == n:
                    res.append(permutation)
                else:
                    permutations.append(permutation)

    return res


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
