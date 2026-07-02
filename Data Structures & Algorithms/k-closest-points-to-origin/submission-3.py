class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        for x,y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(q, (dist, x, y))
        res = []
        while k:
            _,x,y = heapq.heappop(q)
            res.append([x,y])
            k -= 1
        
        return res