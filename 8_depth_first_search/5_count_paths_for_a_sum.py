# 找到所有路径和等于s的路径，只要是up->bottom的都可以，可以不经过root和leaf

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
    # 因为是随便一条路径，所以随便把某个节点作为开始节点
    cur_path.append(root.val)

    # 倒着遍历，正着遍历会让当前节点一直存在
    for i in range(len(cur_path) - 1, -1, -1):
        path_sum += cur_path[i]

        if path_sum == s:
            path_count += 1

    # 递归会让结束节点越来越深，所以前面倒着遍历不影响结束节点
    path_count += count(root.left, s, cur_path)
    path_count += count(root.right, s, cur_path)

    del cur_path[-1]

    return path_count


def count_paths(root, S):
    return f(root, S, [])


def f(root, s, cur_path):
    if not root:
        return 0

    count = 0

    cur_path.append(root.val)
    cur_sum = 0
    for i in range(len(cur_path) - 1, -1, -1):
        cur_sum += cur_path[i]
        if cur_sum == s:
            count += 1
    count += f(root.left, s, cur_path)
    count += f(root.right, s, cur_path)

    del cur_path[-1]
    return count


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 23)))


main()
