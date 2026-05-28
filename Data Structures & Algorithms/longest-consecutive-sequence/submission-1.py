class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for n in seen:
            if n-1 not in seen:
                l = 1
                t = n
                while t+1 in seen:
                    l += 1
                    t += 1
                res = max(res, l)
        return res

        
        