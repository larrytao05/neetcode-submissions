import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        q = [(0,0)]
        visited = set()
        cost = 0
        while len(visited) < n:
            w,ind = heapq.heappop(q)
            if ind in visited:
                continue
            cost += w
            visited.add(ind)
            for i in range(n):
                if i not in visited:
                    x1,y1 = points[ind]
                    x2,y2 = points[i]
                    weight = abs(x2-x1) + abs(y2-y1)
                    heapq.heappush(q, (weight, i))
        return cost
