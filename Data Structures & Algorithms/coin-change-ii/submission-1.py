class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        dp = [0] * (amount+1)
        dp[0] = 1
        for i in range(n-1,-1,-1):
            nextDp = [0] * (amount+1)
            nextDp[0] = 1
            for a in range(amount+1):
                if a >= coins[i]:
                    nextDp[a] = dp[a]
                    nextDp[a] += nextDp[a-coins[i]]
            dp = nextDp
        return dp[amount]