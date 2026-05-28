class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maxProf = 0
        for p in prices:
            if p < lowest:
                lowest = p
            if p - lowest > maxProf:
                maxProf = p - lowest
        return maxProf