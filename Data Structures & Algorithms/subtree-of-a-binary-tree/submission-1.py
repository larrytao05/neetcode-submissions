# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root, node):
            if not root and not node:
                return True
            if not root or not node:
                return False
            if root.val != node.val:
                return False
            return sameTree(root.left, node.left) and sameTree(root.right, node.right)
        
        def findSubtree(root):
            if not root:
                return False
            if root.val == subRoot.val:
                if sameTree(root, subRoot):
                    return True
            return findSubtree(root.left) or findSubtree(root.right)
            
        if not subRoot:
            return True
        if not root:
            return False
        return findSubtree(root)

