import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            q.append([dist, x, y])
        heapq.heapify(q)

        res = []
        for i in range(k):
            dist,x,y = heapq.heappop(q)
            res.append([x,y])
        return res