# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurse(self, root, maxSeen):
        if not root:
            return 0
        total = 0
        if root.val >= maxSeen:
            total += 1
            maxSeen = root.val
            
        total += self.recurse(root.left, maxSeen)
        total += self.recurse(root.right, maxSeen)
        return total

    def goodNodes(self, root: TreeNode) -> int:
        return self.recurse(root, -1 * float('inf'))