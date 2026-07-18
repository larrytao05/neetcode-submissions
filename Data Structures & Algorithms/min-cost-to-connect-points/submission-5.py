class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # minimum spanning tree
        cost = 0
        

        seen = set()
        edges = [(0,0)]
        while len(seen) < len(points):
            w,i = heapq.heappop(edges)
            if i in seen:
                continue
            seen.add(i)
            cost += w

            x,y = points[i]
            for j in range(len(points)):
                if j not in seen:
                    x_1,y_1 = points[j]
                    new_w = abs(x-x_1) + abs(y-y_1)
                    heapq.heappush(edges, (new_w, j))

        return cost
