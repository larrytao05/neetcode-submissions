class Solution:
    def __init__(self):
        self.res = 0

    def recurse(self, root):
        if not root:
            return 0

        left = self.recurse(root.left)
        right = self.recurse(root.right)

        self.res = max(self.res, left + right)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root):
        self.recurse(root)
        return self.res