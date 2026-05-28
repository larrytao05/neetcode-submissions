import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = [math.sqrt(x**2 + y**2) for [x,y] in points]
        q = list(zip(q, points))
        heapq.heapify(q)

        res = []
        for i in range(k):
            dist,pos = heapq.heappop(q)
            x,y = pos
            res.append([x,y])
        return res