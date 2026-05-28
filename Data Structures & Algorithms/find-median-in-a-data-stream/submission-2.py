import heapq

class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2:
            return self.nums[n//2]
        mid = n//2
        return 0.5 * (self.nums[mid] + self.nums[mid-1])
        