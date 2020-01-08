class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_num(root, sum_num):
    if not root:
        return 0

    sum_num = sum_num * 10 + root.val

    if not root.left and not root.right:
        return sum_num

    return find_num(root.left, sum_num) + find_num(root.right, sum_num)


def find_sum_of_path_numbers(root):
    return find_num(root, 0)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
