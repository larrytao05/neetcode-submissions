class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        if len(s) == len(t):
            return 1 if s == t else 0
        dp = [0] * (len(t)+1)
        dp[0] = 1
        for i in range(1,len(s)+1):
            nextDp = [0] * (len(t)+1)
            nextDp[0] = 1
            for j in range(1,len(t)+1):
                nextDp[j] = dp[j]
                if s[i-1] == t[j-1]:
                    nextDp[j] += dp[j-1]
            dp = nextDp
        return dp[len(t)]