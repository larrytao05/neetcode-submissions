class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [1] * (n+1)
        for i in range(2,n+1):
            one = ways[i-1]
            two = ways[i-2]
            ways[i] = one + two
        return ways[n]