class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        dp = defaultdict(int)
        dp[0] = 1
        for i in range(n-1,-1,-1):
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total + nums[i]] += count
                next_dp[total - nums[i]] += count
            dp = next_dp
        return dp[target]
