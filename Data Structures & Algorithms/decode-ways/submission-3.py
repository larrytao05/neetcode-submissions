class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(len(s)):
            cur = int(s[i])
            # start new
            if cur != 0:
                dp[i+1] += dp[i]
            if i > 0 and ((int(s[i-1]) == 1) or (int(s[i-1]) == 2 and 0 <= cur <= 6)):
                dp[i+1] += dp[i-1]
        
        return dp[len(s)]