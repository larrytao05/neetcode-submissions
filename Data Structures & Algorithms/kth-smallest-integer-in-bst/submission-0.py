# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        # inorder traversal
        def inOrder(root):
            nonlocal res
            nonlocal k
            if not root:
                return None
            if root.left:
                inOrder(root.left)
            if k == 1:
                res = root.val
                k -= 1
                return None
            k -= 1
            if root.right:
                inOrder(root.right)
        inOrder(root)
        return res