# 找到树的最大直径，树的直径指的是从一个leaf到另一个leaf的最大长度，可以不经过root


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:

    def __init__(self):
        self.treeDiameter = 0

    def find_diameter(self, root):
        self.depth(root)

        return self.treeDiameter

    def depth(self, root):
        if not root:
            return 0

        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)

        dia = left_depth + right_depth + 1
        self.treeDiameter = max(self.treeDiameter, dia)

        return max(left_depth, right_depth) + 1

    def depth2(self, root):
        if not root:
            return 0

        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        diameter = left_depth + right_depth + 1
        self.treeDiameter = max(self.treeDiameter, diameter)
        return max(left_depth, right_depth) + 1


def main():
    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()
