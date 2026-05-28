class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(n):
            cur = int(s[i])
            prev = int(s[i-1])
            # start new
            if cur != 0:
                dp[i+1] += dp[i]
            if i > 0 and ((prev == 1) or (prev == 2 and 0 <= cur <= 6)):
                dp[i+1] += dp[i-1]
        
        return dp[n]