from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:     
        adj = defaultdict(set)
        n = len(edges)
        def dfs(i):
            visited = set()
            s = [(i,-1)]
            while s:
                cur,par = s.pop()
                for nxt in adj[cur]:
                    if nxt == par:
                        continue
                    if nxt in visited:
                        return True
                    s.append((nxt,cur))
                    visited.add(nxt)
            return False
        for u,v in edges:
            adj[u].add(v)
            adj[v].add(u)
            if dfs(u):
                return [u,v]
        return []



