class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(n):
            maxJ = nums[i]
            for j in range(i+1,min(i+maxJ+1, n)):
                dp[j] = min(dp[j], dp[i]+1)
        return dp[n-1]