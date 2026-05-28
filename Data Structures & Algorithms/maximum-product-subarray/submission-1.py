class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        globalMax = nums[0]
        curMin = curMax = 1

        for num in nums:
            tmp = curMax*num
            curMax = max(num, curMax*num, curMin*num)
            curMin = min(num, tmp, curMin*num)
            globalMax = max(globalMax, curMax)
        return globalMax
