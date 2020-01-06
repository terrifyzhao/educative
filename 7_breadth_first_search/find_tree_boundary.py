from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_tree_boundary(root):
    result = []

    if not root:
        return result

    queue = deque()
    queue.append(root)

    left_view = []
    right_view = deque()
    # leaf_view = []

    while queue:
        len_queue = len(queue)

        for i in range(len_queue):
            cur_node = queue.popleft()
            if cur_node.left is None and cur_node.right is None:
                continue
            elif i == 0:
                left_view.append(cur_node)
            elif i == len_queue - 1:
                right_view.appendleft(cur_node)

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

    return left_view + dfs(root) + list(right_view)


def dfs(root):
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        cur_node = queue.pop()

        if not cur_node.left and not cur_node.right:
            res.append(cur_node)
        if cur_node.right:
            queue.append(cur_node.right)
        if cur_node.left:
            queue.append(cur_node.left)
    return res


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(9)
    root.left.right = TreeNode(3)
    root.left.right.left = TreeNode(15)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(6)
    result = find_tree_boundary(root)
    print("Tree boundary: ", end='')
    for node in result:
        print(str(node.val) + " ", end='')


main()
