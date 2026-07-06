# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def helper(root):
            nonlocal res
            if not root:
                return 0
            left = max(helper(root.left), 0)
            right = max(helper(root.right), 0)
            cur = max(left + root.val + right, left + root.val, right + root.val)
            res = max(cur, res)
            return max(left, right, 0) + root.val
        helper(root)
        return res
            
