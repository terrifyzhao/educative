from collections import deque


def find_permutations(nums):
    result = []
    nums_len = len(nums)
    permutation = deque()
    permutation.append([])
    for num in nums:
        n = len(permutation)

        for i in range(n):
            old_permutation = permutation.popleft()

            # 创建一个新的permutation，在每个位置都插入num
            for j in range(len(old_permutation) + 1):
                new_permutation = list(old_permutation)
                new_permutation.insert(j, num)
                if len(new_permutation) == nums_len:
                    result.append(new_permutation)
                else:
                    permutation.append(new_permutation)
    return result


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
