class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seqs = {}
        best = -1
        for n in nums:
            if n-1 not in nums:
                seqs[n] = 1
                curLen = 0
                while n+curLen in nums:
                    curLen += 1
                best = max(best,curLen)
            
        return max(best,0)

                