class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = [-1 * i for i in nums[:k]]
        heapq.heapify(heap)
        window = Counter(nums[:k])
        res.append(-1*heap[0])
        for r in range(k,len(nums)):
            window[nums[r-k]] -= 1
            window[nums[r]] += 1
            heapq.heappush(heap, -1 * nums[r])
            while heap and window[-1*heap[0]] == 0:
                heapq.heappop(heap)
            res.append(-1 *heap[0])
        return res