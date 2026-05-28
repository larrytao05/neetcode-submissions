# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')
        def helper(root, acc):
            nonlocal res
            if not root:
                return 0
            left = helper(root.left, acc + root.val)
            right = helper(root.right, acc + root.val)
            best = max(root.val, left + root.val + right, left + root.val + acc, right + root.val + acc, left + root.val, right + root.val)
            res = max(res, best)
            return max(root.val, left + root.val, right + root.val)
        helper(root, 0)
        return res
