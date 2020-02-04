class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_trees(n):
    if n <= 1:
        return 1
    count = 0
    for i in range(1, n + 1):
        left = count_trees(i - 1)
        right = count_trees(n - i)
        count += (left * right)

    return count


def count_trees(n):
    if n <= 1:
        return 1
    count = 0
    for i in range(1, n + 1):
        l = count_trees(i - 1)
        r = count_trees(n - i)
        count += (l * r)

    return count


def main():
    print("Total trees: " + str(count_trees(2)))
    print("Total trees: " + str(count_trees(3)))


main()
