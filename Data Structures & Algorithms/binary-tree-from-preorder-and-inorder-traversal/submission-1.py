# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preOrder = 0
        i = 0
        def helper(lim):
            nonlocal preOrder
            nonlocal i
            if preOrder >= len(preorder):
                return None
            if inorder[i] == lim:
                i += 1
                return None
            root = TreeNode(preorder[preOrder])
            preOrder += 1
            root.left = helper(root.val)
            root.right = helper(lim)
            return root
        return helper(math.inf)