from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [(-1*cnt,n) for n,cnt in Counter(nums).items()]
        heapq.heapify(heap)
        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res
