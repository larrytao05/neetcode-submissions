from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freqs = defaultdict(int)
        for c in s:
            freqs[c] += 1
        res = []
        curLen = 0
        seen = {}
        for c in s:
            if c in seen and seen[c] > 0:
                seen[c] -= 1
                if seen[c] == 0:
                    seen.pop(c)
            elif freqs[c] > 1:
                seen[c] = freqs[c] - 1
            curLen += 1
            if len(seen) == 0:
                res.append(curLen)
                curLen = 0
                seen = {}

        return res