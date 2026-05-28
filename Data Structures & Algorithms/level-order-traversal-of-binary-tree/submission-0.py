from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        if not root:
            return res
        q.append((root, 0))
        level = 0
        currLevel = []
        while q:
            node, lvl = q.popleft()
            if level != lvl:
                res.append(currLevel)
                currLevel = []
                level +=1
            currLevel.append(node.val)
            if node.left:
                q.append((node.left, lvl+1))
            if node.right:
                q.append((node.right, lvl+1))
        if currLevel:
            res.append(currLevel)
        return res

