from collections import deque,defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((v,t))
        q = deque([k])
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        while q:
            nxt = q.popleft()
            for nei,weight in adj[nxt]:
                print(nei)
                print(weight)
                if dist[nxt] + weight < dist[nei]:
                    dist[nei] = dist[nxt] + weight
                    q.append(nei)
        maxTime = 0
        for ind,time in enumerate(dist):
            if ind == 0:
                continue
            print(time)
            if time == float('inf'):
                return -1
            maxTime = max(maxTime, time)
        return maxTime