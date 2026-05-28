# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def countGood(root, greatest):
            if not root:
                return 0
            greatest = max(greatest, root.val)
            if greatest <= root.val:
                return countGood(root.left, greatest) + countGood(root.right, greatest) + 1
            return countGood(root.left, greatest) + countGood(root.right, greatest)
        return countGood(root, -math.inf)