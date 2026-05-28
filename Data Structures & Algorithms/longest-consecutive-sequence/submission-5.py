class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starts = {}
        mod = set(nums)
        res = 0
        for n in mod:
            if (n-1) not in mod:
                length = 1
                cur = n
                while n+length in mod:
                    length += 1
                res = max(res, length)
                n += length
        return res

        