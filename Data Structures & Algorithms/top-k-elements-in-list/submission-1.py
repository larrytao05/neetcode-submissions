class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = [(v,k) for k,v in counts.items()]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        return [x[1] for x in heap]