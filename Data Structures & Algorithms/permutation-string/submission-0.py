class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counts = [0] * 26
        counts2 = [0] * 26
        for i,c in enumerate(s1):
            counts[ord(c)-ord('a')] += 1
            counts2[ord(s2[i])-ord('a')] += 1
        
        l = 0
        remaining = 0
        for i in range(26):
            if counts[i] == counts2[i]:
                remaining += 1
        for r in range(len(s1), len(s2)):
            if remaining == 26:
                return True
            i = ord(s2[r]) - ord('a')
            counts2[i] += 1
            if counts2[i] == counts[i]:
                remaining += 1
            elif counts[i] + 1 == counts2[i]:
                remaining -= 1
            
            i = ord(s2[l]) - ord('a')
            counts2[i] -= 1
            if counts2[i] == counts[i]:
                remaining += 1
            elif counts2[i] + 1 == counts[i]:
                remaining -= 1
            l += 1
        return remaining == 26
