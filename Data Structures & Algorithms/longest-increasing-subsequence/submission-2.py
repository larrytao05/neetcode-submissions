class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * (n+1)

        best = 0

        for i in range(n):
            for last in range(i):
                if nums[i] > nums[last]:
                    dp[i] = max(dp[i], dp[last] + 1)
            best = max(dp[i], best)
        return best