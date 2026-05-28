from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        for i in range(len(s)):
            if s[i] not in sdict:
                sdict[s[i]] = 1
            else:
                sdict[s[i]] += 1
        
        for j in range(len(t)):
            if t[j] not in tdict:
                tdict[t[j]] = 1
            else:
                tdict[t[j]] += 1
        return tdict == sdict


        
        


