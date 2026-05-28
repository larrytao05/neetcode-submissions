class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l,r = 0, 0
        res = 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                res = max(res, r-l)
            else:
                
                while l <= r and s[l] != s[r]:
                    if s[l] in seen:
                        seen.remove(s[l])
                    l += 1
                l += 1
                r += 1
        return res
                