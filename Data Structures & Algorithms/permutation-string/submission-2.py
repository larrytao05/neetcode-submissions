class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnts = Counter(s1)
        s2_cnts = Counter(s2[:len(s1)])
        r = len(s1)
        l = 0

        if s1_cnts == s2_cnts:
                return True

        while r < len(s2):
            s2_cnts[s2[l]] -= 1
            if s2[r] in s2_cnts:
                s2_cnts[s2[r]] += 1
            else:
                s2_cnts[s2[r]] = 1
            if s1_cnts == s2_cnts:
                return True
            r += 1
            l += 1
        return False
