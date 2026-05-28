import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = nums
        heapq.heapify(q)
        target = len(nums) - k
        while target > 0:
            heapq.heappop(q)
            target -= 1
        return q[0]