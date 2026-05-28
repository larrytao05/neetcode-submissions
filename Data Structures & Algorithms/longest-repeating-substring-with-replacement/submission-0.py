class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        current = 0
        seen = defaultdict(int)
        l=0
        
        for r in range(len(s)):
            seen[s[r]] += 1
            current = max(current, seen[s[r]])
            while (r-l+1) - current > k:
                seen[s[l]] -=1
                l+=1
            maxLen = max(maxLen, r-l+1)
        return maxLen