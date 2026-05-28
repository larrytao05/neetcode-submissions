from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def bfs(start):
            if not start:
                return None
            visited = {start.val:Node(start.val)}
            q = deque()
            q.append(start)
            while q:
                cur = q.popleft()
                new_cur = visited[cur.val]
                for n in cur.neighbors:
                    if n.val not in visited:
                        temp = Node(n.val)
                        new_cur.neighbors.append(temp)
                        visited[n.val] = temp
                        q.append(n)
                    else:
                        new_cur.neighbors.append(visited[n.val])
            return visited[start.val]
        return bfs(node)
