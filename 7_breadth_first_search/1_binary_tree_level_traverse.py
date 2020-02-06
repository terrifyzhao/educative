from collections import deque

# 广度遍历

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    if not root:
        return root
    result = []

    queue = deque()
    queue.append(root)

    while queue:

        queue_len = len(queue)
        cur_level = []
        for _ in range(queue_len):
            cur_node = queue.popleft()
            cur_level.append(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        result.append(cur_level)

    return result


def traverse(root):
    res = []
    if root is None:
        return res

    queue = deque()
    queue.append(root)

    while queue:
        queue_size = len(queue)
        level = []
        for _ in range(queue_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    return res


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
