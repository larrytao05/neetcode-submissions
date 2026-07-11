class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        maxHeap = []
        minHeap = []
        for n in nums1:
            if not maxHeap or -1 * maxHeap[0] >= n:
                heapq.heappush(maxHeap, -1*n)
                if abs(len(maxHeap) - len(minHeap)) > 1:
                    heapq.heappush(minHeap, heapq.heappop(maxHeap) * -1)
            else:
                heapq.heappush(minHeap, n)
                if abs(len(maxHeap) - len(minHeap)) > 1:
                    heapq.heappush(maxHeap, heapq.heappop(minHeap) * -1)
        for n in nums2:
            if not maxHeap or -1 * maxHeap[0] >= n:
                heapq.heappush(maxHeap, -1*n)
                if abs(len(maxHeap) - len(minHeap)) > 1:
                    heapq.heappush(minHeap, heapq.heappop(maxHeap) * -1)
            else:
                heapq.heappush(minHeap, n)
                if abs(len(maxHeap) - len(minHeap)) > 1:
                    heapq.heappush(maxHeap, heapq.heappop(minHeap) * -1)
        
        if len(maxHeap) > len(minHeap):
            return maxHeap[0] * -1
        elif len(minHeap) > len(maxHeap):
            return minHeap[0]
        else:
            return (minHeap[0] + (-1 * maxHeap[0])) / 2.0
