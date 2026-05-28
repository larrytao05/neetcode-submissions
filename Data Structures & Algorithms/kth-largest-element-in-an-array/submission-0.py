import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = nums
        heapq.heapify(q)
        k = len(nums)-k+1
        for i in range(k):
            if i == k-1:
                return heapq.heappop(q)
            heapq.heappop(q)