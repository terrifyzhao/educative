from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    depth = 0
    if not root:
        return 0

    queue = deque()
    queue.append(root)

    while queue:
        len_queue = len(queue)
        depth += 1
        for _ in range(len_queue):
            cur_node = queue.popleft()

            if not cur_node.left and not cur_node.right:
                return depth

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)

    return depth


def find_minimum_depth(root):
    if not root:
        return 0

    min_length = 0
    queue = deque()
    queue.append(root)

    while queue:
        queue_size = len(queue)
        min_length+=1
        for _ in range(queue_size):
            node = queue.popleft()

            if not node.left and node.right:
                return min_length

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return min_length



def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
