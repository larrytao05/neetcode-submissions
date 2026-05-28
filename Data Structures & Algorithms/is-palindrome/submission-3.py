class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for c in s:
            if ((48 <= ord(c) < 58) or (65 <= ord(c) < 91) or (97 <= ord(c) < 123)):
                cleaned += c.lower()
        midpt = len(cleaned) // 2
        if len(cleaned) % 2 == 0:
            return cleaned[:midpt] == cleaned[midpt:][::-1]
        return cleaned[:midpt] == cleaned[midpt+1:][::-1]