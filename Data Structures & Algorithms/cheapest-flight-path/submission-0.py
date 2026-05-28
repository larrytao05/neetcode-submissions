from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = [[] for _ in range(n)]
        for i,j,w in flights:
            edges[i].append([j,w])
        cost = [float('inf')] * n
        cost[src] = 0
        q = deque([(0,src,0)])
        while q:
            cst,node,steps = q.popleft()
            if steps > k:
                continue
            for nei,w in edges[node]:
                if cst + w < cost[nei]:
                    cost[nei] = cst + w
                    q.append((cst + w, nei, steps+1))
        return cost[dst] if cost[dst] != float('inf') else -1

        
        