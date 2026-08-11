import heapq


class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None: 
        if not self.left or num <= self.left[0] * -1:
            heapq.heappush(self.left, -1 * num)
            if len(self.left) > len(self.right) + 1:
                heapq.heappush(self.right, heapq.heappop(self.left) * -1)
        else:
            heapq.heappush(self.right, num)
            if len(self.right) > len(self.left) + 1:
                heapq.heappush(self.left, heapq.heappop(self.right) * -1)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.left[0] * -1 + self.right[0]) / 2.0
        elif len(self.left) > len(self.right):
            return self.left[0] * -1
        return self.right[0]