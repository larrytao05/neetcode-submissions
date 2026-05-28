class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starts = {}
        mod = set(nums)
        res = 0
        for n in mod:
            if (n-1) not in mod:
                length = 1
                cur = n
                while n+1 in mod:
                    length += 1
                    n += 1
                res = max(res, length)
        return res

        