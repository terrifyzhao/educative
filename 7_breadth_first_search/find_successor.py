from collections import deque


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

        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)

        if key == cur_node.val:
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
