class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = set()
        l = 0
        r = 0
        res = 0

        while r < len(s):
            if s[r] not in cur:
                cur.add(s[r])
                r += 1
                res = max(res, r-l)
            else:
                while s[r] in cur:
                    cur.remove(s[l])
                    l += 1
                cur.add(s[r])
                r += 1
        return res