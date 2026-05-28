class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxLen = 0
        for n in s:
            if n-1 in s:
                continue
            temp = n
            currLen = 0
            while temp in s:
                currLen += 1
                temp += 1
            if currLen > maxLen:
                maxLen = currLen
        return maxLen