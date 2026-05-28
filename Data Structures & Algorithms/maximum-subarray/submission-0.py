class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = -math.inf
        for n in nums:
            if n > curSum +n:
                curSum = n
            else:
                curSum += n
            maxSum = max(curSum,maxSum)
        return maxSum
            