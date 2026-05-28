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
            if left < 0 and right < 0:
                res = max(res, root.val)
            elif left < 0:
                res = max(res, root.val + right)
            elif right < 0:
                res = max(res, root.val + left)
            else:
                res = max(res, left + root.val + right)
            return root.val + max(left, right, 0)
        helper(root)
        return res