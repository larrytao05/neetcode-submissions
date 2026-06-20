class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def compare_cnts(cnt1, cnt2):
            for k,v in cnt1.items():
                if v > 0:
                    if k not in cnt2 or cnt2[k] != v:
                        return False
            
            for k,v in cnt2.items():
                if v > 0:
                    if k not in cnt1 or cnt1[k] != v:
                        return False
            return True
        s1_cnts = Counter(s1)
        s2_cnts = Counter(s2[:len(s1)])
        r = len(s1)
        l = 0

        if compare_cnts(s1_cnts, s2_cnts):
                return True

        while r < len(s2):
            s2_cnts[s2[l]] -= 1
            if s2[r] in s2_cnts:
                s2_cnts[s2[r]] += 1
            else:
                s2_cnts[s2[r]] = 1
            if compare_cnts(s1_cnts, s2_cnts):
                return True
            r += 1
            l += 1
        return False
