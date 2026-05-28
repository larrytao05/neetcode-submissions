class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       # start with length of 1
        if len(s) == 0:
            return 0
        maxLen = 0
        seen = set()
        l,r = 0,0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
            else:
                maxLen = max(maxLen, r-l)
                while l < r and s[l] != s[r]:
                    if s[l] in seen:
                        seen.remove(s[l])
                    l+=1
                l+=1
                r+=1
        return max(maxLen, r-l) 