class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l,r = 0,0
        res = 0
        while r < len(s):
            if s[r] not in seen:
                res = max(res, r-l+1)
                seen.add(s[r])
                r += 1
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
                r += 1
        return res