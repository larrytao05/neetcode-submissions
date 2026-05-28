# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, maxVal):
            if not root:
                return 0
            total = 0
            if maxVal <= root.val:
                total += 1
                maxVal = root.val
            total += helper(root.left, maxVal)
            total += helper(root.right, maxVal)
            return total
        return helper(root, -1 * math.inf)