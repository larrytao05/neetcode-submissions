class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * (n)
        
        for i in range(1,m+1):
            nextDp = [0] * (n)
            nextDp[0] = 1
            for j in range(1,n):
                nextDp[j] += nextDp[j-1] + dp[j]
                # print(f"currently at ({i}, {j})")
                # print(f"number of paths: {nextDp[j]}")
            dp = nextDp
        return dp[n-1]