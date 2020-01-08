class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    return count(root, S, [])


def count(root, s, cur_path):
    if not root:
        return 0

    path_sum = 0
    path_count = 0
    cur_path.append(root.val)

    for i in range(len(cur_path) - 1, -1, -1):
        path_sum += cur_path[i]

        if path_sum == s:
            path_count += 1

    path_count += count(root.left, s, cur_path)
    path_count += count(root.right, s, cur_path)

    del cur_path[-1]

    return path_count


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 23)))


main()
