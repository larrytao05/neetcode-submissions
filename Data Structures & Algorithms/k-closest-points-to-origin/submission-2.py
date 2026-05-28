import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        for x,y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(q, (-dist,x,y))
            if len(q) > k:
                heapq.heappop(q)
        return [[p[1],p[2]] for p in q]