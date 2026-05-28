import heapq


class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.right or num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -1 * num)
        if abs(len(self.right) - len(self.left)) > 1:
            if len(self.right) > len(self.left):
                temp = heapq.heappop(self.right)
                heapq.heappush(self.left, -temp)
            else:
                temp = heapq.heappop(self.left)
                heapq.heappush(self.right, -temp)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            l = -1 * self.left[0]
            r = self.right[0]
            return (l+r)/2.0
        else:
            if len(self.left) > len(self.right):
                return -1 * self.left[0]
            return self.right[0]
        