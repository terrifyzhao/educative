from __future__ import print_function
from collections import deque


# 把所有节点按照顺序连在一起


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # tree traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def connect_all_siblings(root):
    if not root:
        return

    queue = deque()
    queue.append(root)
    pre_node, cur_node = None, None
    while queue:
        cur_node = queue.popleft()

        if pre_node:
            pre_node.next = cur_node
        pre_node = cur_node

        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)

    return


def connect_all_siblings(root):
    res = []
    if root is None:
        return res

    queue = deque()
    queue.append(root)
    pre_node = None
    while queue:
        node = queue.popleft()
        if pre_node:
            pre_node.next = node
        pre_node = node

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)
    root.print_tree()


main()
