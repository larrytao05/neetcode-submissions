from collections import deque, defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        components = 0
        edgeMap = defaultdict(set)
        for x,y in edges:
            edgeMap[x].add(y)
            edgeMap[y].add(x)
        def bfs(i):
            nonlocal components
            q = deque()
            q.append(i)
            visited.add(i)
            components += 1
            while q:
                nxt = q.popleft()
                for nbr in edgeMap[nxt]:
                    if nbr not in visited:
                        q.append(nbr)
                        visited.add(nbr)
        for ind in range(n):
            if ind not in visited:
                bfs(ind)
        return components
                