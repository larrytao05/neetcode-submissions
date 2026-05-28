from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u-1].append((v-1,t))
        q = [(0,k-1)]
        visit = set()
        t=0
        while q:
            weight,nxt = heapq.heappop(q)
            if nxt in visit:
                continue
            visit.add(nxt)
            t = weight
            for nei,weight2 in adj[nxt]:
                if nei not in visit:
                    heapq.heappush(q, (weight + weight2, nei))
 
        return t if len(visit) == n else -1