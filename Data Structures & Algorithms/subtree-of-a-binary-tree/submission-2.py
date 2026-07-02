# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        if not self.isSameTree(p.left, q.left):
            return False
        return self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root.left:
            if self.isSubtree(root.left, subRoot):
                return True
        if root.right:
            if self.isSubtree(root.right, subRoot):
                return True
        if self.isSameTree(root, subRoot):
            return True
        return False
        
