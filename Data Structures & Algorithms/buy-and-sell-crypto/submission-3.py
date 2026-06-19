class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = math.inf
        best = 0

        for p in prices:
            if p-low > best:
                best = p-low
            if p < low:
                low = p
        
        return best