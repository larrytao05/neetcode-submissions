"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        st = deque()
        st.appendleft(node)
        seen = {}
        root = Node(node.val)
        seen[node.val] = root
        while st:
            nxt = st.pop()
            new = seen[nxt.val]
            if not root:
                root = new
            for n in nxt.neighbors:
                if n.val not in seen:
                    st.appendleft(n)
                    seen[n.val] = Node(n.val)
                new.neighbors.append(seen[n.val])
        return root
