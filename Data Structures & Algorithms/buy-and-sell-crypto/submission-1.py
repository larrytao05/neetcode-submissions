class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = math.inf
        res = 0
        for n in prices:
            res = max(res, n - smallest)
            if n < smallest:
                smallest = n
        return res