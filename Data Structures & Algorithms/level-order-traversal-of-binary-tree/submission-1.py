# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if not root:
            return []
        q.append((root, 1))
        res = []
        lvl = 0

        while q:
            cur, curLevel = q.popleft()
            if curLevel > lvl:
                lvl += 1
                res.append([])
            if cur.left:
                q.append((cur.left, curLevel + 1))
            if cur.right:
                q.append((cur.right, curLevel + 1))
            res[-1].append(cur.val)
        return res


