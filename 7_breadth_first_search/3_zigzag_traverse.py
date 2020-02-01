from collections import deque


# 锯齿广度遍历

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    if not root:
        return result

    queue = deque()
    queue.append(root)
    left_to_right = True
    while queue:
        len_queue = len(queue)
        cur_level = deque()

        for _ in range(len_queue):
            cur_node = queue.popleft()
            if left_to_right:
                cur_level.append(cur_node.val)
            else:
                cur_level.appendleft(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        left_to_right = not left_to_right
        result.append(list(cur_level))

    return result


def traverse(root):
    res = []
    if root is None:
        return res

    queue = deque()
    queue.append(root)
    i = 0
    while queue:
        queue_size = len(queue)
        level = deque()
        for _ in range(queue_size):
            node = queue.popleft()

            if i & 1 == 0:
                level.append(node.val)
            else:
                level.appendleft(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        i += 1
        res.append(list(level))

    return res


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
