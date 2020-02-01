# 找到所有从根到叶子节点的路径，其和等于sum

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    allPaths = []
    find(root, [], allPaths, sum)

    return allPaths


def find(root, cur_path, all_path, sum):
    if not root:
        return
    cur_path.append(root.val)

    if root.val == sum and not root.left and not root.right:
        all_path.append(list(cur_path))
    else:
        find(root.left, cur_path, all_path, sum - root.val)
        find(root.right, cur_path, all_path, sum - root.val)
    # 遍历完了要回溯
    del cur_path[-1]


def find_paths(root, sum):
    all = []
    f(root, sum, [], all)
    return all


def f(root, sum, cur, all):
    if not root:
        return
    cur.append(root.val)
    if root.val == sum and root.left is None and root.right is None:
        all.append(list(cur))
    else:
        f(root.left, sum - root.val, cur, all)
        f(root.right, sum - root.val, cur, all)

    del cur[-1]


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))


main()
