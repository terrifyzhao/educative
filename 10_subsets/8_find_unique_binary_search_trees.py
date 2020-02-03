# 给定一个数字，返回所有的二叉搜索树


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_unique_trees(n):
    if n <= 0:
        return []

    return find_unique_trees_r(1, n)


def find_unique_trees_r(start, end):
    result = []

    if start > end:
        result.append(None)
        return result

    for i in range(start, end + 1):
        left = find_unique_trees_r(start, i - 1)
        right = find_unique_trees_r(i + 1, end)

        for l in left:
            for r in right:
                root = TreeNode(i)
                root.left = l
                root.right = r
                result.append(root)

    return result


def find_unique_trees_r(start, end):
    res = []
    if start > end:
        res.append(None)
        return res

    for i in range(start, end+1):
        left = find_unique_trees_r(start, i-1)
        right = find_unique_trees_r(i+1, end)

        for l in left:
            for r in right:
                root = TreeNode(i)
                root.left = l
                root.right = r
                res.append(root)

    return res


def main():
    print("Total trees: " + str(len(find_unique_trees(2))))
    print("Total trees: " + str(len(find_unique_trees(3))))


main()
