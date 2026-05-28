from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        counts = defaultdict(int)
        counts2 = defaultdict(int)
        matches = 0
        for i in range(len(t)):
            counts[t[i]] += 1
        have, need = 0,len(counts)
        minLen = math.inf
        res = 0
        l =0
        for r in range(len(s)):
            c = s[r]
            counts2[c] += 1

            if c in counts and counts[c] == counts2[c]:
                have += 1
            while have == need:
                if (r-l+1) < minLen:
                    minLen = r-l+1
                    start = l
                counts2[s[l]] -= 1
                if s[l] in counts and counts[s[l]] > counts2[s[l]]:
                    have -= 1
                l += 1
        return s[start:start + minLen] if minLen != math.inf else ""
        