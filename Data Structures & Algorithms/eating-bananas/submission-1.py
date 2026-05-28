import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def test_k(k):
            res = 0
            for n in piles:
                res += math.ceil(n / k)
            return res
        l,r = 1,max(piles)
        k = r
        while l <= r:
            mdpt = (l+r) // 2
            hours = test_k(mdpt)
            if hours > h:
                l = mdpt+1
            elif hours <= h:
                k = mdpt
                r = mdpt-1
        return k

