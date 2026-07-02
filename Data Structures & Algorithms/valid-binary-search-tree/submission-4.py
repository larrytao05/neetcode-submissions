# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checker(root, minV, maxV):
            if not root:
                return True
            if root.val <= minV or root.val >= maxV:
                return False
            if not checker(root.left, minV, min(maxV, root.val)):
                return False
            if not checker(root.right, max(minV, root.val), maxV):
                return False
            return True
        return checker(root, float("-inf"), float("inf"))