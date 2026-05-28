import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counts = defaultdict(int)
        res = []
        for n in nums:
            counts[n] += 1
        for key in counts:
            heapq.heappush(heap, (-counts[key], key))
        counter = k
        while k > 0:
            temp = heapq.heappop(heap)
            res.append(temp[1])
            k -= 1
        return res