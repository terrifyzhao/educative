from collections import deque


# 找到key节点的右侧节点

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_successor(root, key):
    if not root or not key:
        return None

    queue = deque()
    queue.append(root)

    while queue:
        cur_node = queue.popleft()
        # 这里不需要循环queue的size个数，因为不需要统计每层有几个元素
        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)

        if key == cur_node.val:
            break

    return queue[0] if queue else None


def find_successor2(root, key):
    if not root or key is None:
        return root

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        if node.val == key:
            break
    return queue[0] if queue else None


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)


main()
