import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-x for x in stones]
        heapq.heapify(q)
        while len(q) > 1:
            x, y = -1 * heapq.heappop(q), -1 * heapq.heappop(q)
            if x == y:
                continue
            else:
                new_x = min(x, y)
                new_y = max(x, y)
                heapq.heappush(q, -1 * (new_y - new_x))
        if q:
            return q[0] * -1
        return 0
