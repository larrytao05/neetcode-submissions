# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = preorder[0]
        idx = inorder.index(root)
        rootNode = TreeNode(val=root)
        rootNode.left = self.buildTree(preorder[1:1+idx], inorder[:idx])
        rootNode.right = self.buildTree(preorder[1+idx:], inorder[1+idx:])
        return rootNode
