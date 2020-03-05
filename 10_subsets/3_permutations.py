from collections import deque


# 数组的排列组合
def find_permutations(nums):
    result = []
    nums_len = len(nums)
    permutation = deque()
    permutation.append([])
    for num in nums:
        n = len(permutation)
        # 这一层的遍历是遍历所有的permutations
        for _ in range(n):
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


def find_permutations2(nums):
    num_len = len(nums)
    res = []
    queue = deque()
    queue.append([])
    for n in nums:
        l = len(queue)
        for i in range(l):
            tmp = queue.popleft()
            for j in range(len(tmp)+1):
                new_tmp = list(tmp)
                new_tmp.insert(j, n)
                if len(new_tmp) == num_len:
                    res.append(new_tmp)
                else:
                    queue.append(new_tmp)

    return res


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))
    print("Here are all the permutations: " + str(find_permutations2([1, 3, 5])))


main()
