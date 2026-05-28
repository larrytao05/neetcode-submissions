from collections import deque,defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u-1].append((v-1,t))
        q = deque([k-1])
        dist = [float('inf')] * (n)
        dist[k-1] = 0
        while q:
            nxt = q.popleft()
            for nei,weight in adj[nxt]:
                if dist[nxt] + weight < dist[nei]:
                    dist[nei] = dist[nxt] + weight
                    q.append(nei)
        maxTime = 0
        for ind,time in enumerate(dist):
            if time == float('inf'):
                return -1
            maxTime = max(maxTime, time)
        return maxTime