class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * s for s in stones]
        heapq.heapify(stones)
        stlen = len(stones)
        while stlen > 1:
            st1, st2 = heapq.heappop(stones), heapq.heappop(stones)
            if st1 < st2:
                heapq.heappush(stones, st1 - st2)
            elif st2 < st1:
                heapq.heappush(stones, st2 - st1)
            stlen = len(stones)
        return -1 * stones[0] if stlen == 1 else 0
            