import heapq


class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left or num > abs(self.left[0]):
            heapq.heappush(self.right, num)
            if len(self.right) > len(self.left) + 1:
                temp = heapq.heappop(self.right)
                heapq.heappush(self.left, -temp)
        else:
            heapq.heappush(self.left, -num)
            if len(self.left) > len(self.right) + 1:
                temp = heapq.heappop(self.left)
                heapq.heappush(self.right, -temp)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        else:
            if len(self.left) > len(self.right):
                return -self.left[0]
            else:
                return self.right[0]
        
        