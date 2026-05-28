from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       counts = defaultdict(int)
       for c in s:
            counts[c] += 1
       for c in t:
            if counts[c] < 1:
                return False
            else:
                counts[c] -= 1
                if counts[c] == 0:
                    counts.pop(c, None)
       if len(counts) > 0:
        return False
       return True