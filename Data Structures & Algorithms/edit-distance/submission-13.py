class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if n < m:
            m,n = n,m
            word1,word2 = word2,word1
        dp = [0] * (m+1)
        nextDp = [0] * (m+1)
        for i in range(m+1):
            dp[i] = i
        for i in range(1,n+1):
            nextDp[0] = i
            for j in range(1,m+1):
                if word1[i-1] != word2[j-1]:
                    nextDp[j] = 1 + min(dp[j-1], dp[j], nextDp[j-1])
                else:
                    nextDp[j] = dp[j-1]
            dp = nextDp[:]
        return dp[m]

