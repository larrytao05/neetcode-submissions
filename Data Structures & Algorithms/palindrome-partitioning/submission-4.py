class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(s,l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        def helper(i, acc):
            if i >= len(s):
                res.append(acc[:])
                return
            for j in range(i, len(s)):
                if isPalindrome(s,i,j):
                    acc.append(s[i:j+1])
                    helper(j+1, acc)
                    acc.pop()          
        helper(0, [])
        return res