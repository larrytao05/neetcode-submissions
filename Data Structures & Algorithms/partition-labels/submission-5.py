class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        l = r = 0
        counts = Counter(s)
        while r < len(s):
            seen = set()
            seen.add(s[r])
            while r < len(s) and len(seen) > 0:
                if s[r] not in seen:
                    seen.add(s[r])
                counts[s[r]] -= 1
                if counts[s[r]] == 0:
                    seen.remove(s[r])
                r += 1
            res.append(r-l)
            l=r
        return res