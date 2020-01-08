class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    if not root:
        return False

    if root.val == sequence[0] and not root.left and not root.right:
        return True
    if root.val != sequence[0]:
        return False

    return find_path(root.left, sequence[1:]) or find_path(root.right, sequence[1:])


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 5])))
    print("Tree has path sequence: " + str(find_path(root, [1, 0, 6])))
    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 0, 1])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 5])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
