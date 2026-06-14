class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned = ""
        for c in s:
            if c.isalnum():
                cleaned += c
        s = cleaned
        mid = len(s)//2

        if len(s)%2:
            return s[:mid] == s[mid+1:][::-1]
        return s[:mid] == s[mid:][::-1]