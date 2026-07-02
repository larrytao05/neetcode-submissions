# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = 0
    def recurse(self, root, height):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        leftMax = self.recurse(root.left, height + 1)
        rightMax = self.recurse(root.right, height + 1)
        
        
        total = max(leftMax + rightMax, leftMax + height, rightMax + height)
        
        if total > self.res:
            self.res = total
        
        return max(leftMax, rightMax) + 1


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.recurse(root, 0)
        return self.res