from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = Counter(s)
        res = []
        l = 0
        current_set = {}
        for i,c in enumerate(s):
            if c in current_set:
                current_set[c] += 1
            else:
                current_set[c] = 1
            if current_set[c] == counts[c]:
                del current_set[c]
            if len(current_set) == 0:
                res.append(i-l+1)
                l = i+1
        return res