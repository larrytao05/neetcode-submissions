# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        def recurse(root):
            if not root:
                return
            recurse(root.left)
            print(root.val)
            
            if self.k == 1:
                self.res = root.val
            self.k -= 1
            return recurse(root.right)
        recurse(root)
        return self.res