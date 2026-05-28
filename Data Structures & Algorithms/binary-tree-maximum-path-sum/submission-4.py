# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res= -1 * math.inf
        def helper(root):
            nonlocal res
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            res = max(res, left + root.val + right, root.val + right, root.val + left, root.val)
            return root.val + max(left, right, 0)
        helper(root)
        return res