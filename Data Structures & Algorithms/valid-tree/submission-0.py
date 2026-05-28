from collections import deque, defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeMap = defaultdict(set)
        for a,b in edges:
            edgeMap[a].add(b)
            edgeMap[b].add(a)
        def bfs(start):
            visited = set()
            q = deque()
            q.append((start, None))
            visited.add(start)
            while q:
                nxt,prev = q.popleft()
                print(nxt)
                for nbr in edgeMap[nxt]:
                    if nbr != prev and nbr in visited:
                        return False
                    if nbr != prev:
                        visited.add(nbr)
                        q.append((nbr,nxt))
            return len(visited) == n
        return bfs(0)