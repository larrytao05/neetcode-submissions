class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [False] * (m+1)
        dp[0] = True
        for j in range(2, m + 1):
            if p[j - 1] == '*':
                dp[j] = dp[j - 2]
        for i in range(1,n+1):
            nextDp = [False] * (m+1)
            nextDp[0] = False
            for j in range(1, m+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    nextDp[j] = dp[j-1]
                elif p[j-1] == "*":
                    nextDp[j] = nextDp[j - 2]
                    if s[i-1] == p[j-2] or p[j-2] == '.':
                        nextDp[j] |= dp[j]
            dp = nextDp
        return dp[m]