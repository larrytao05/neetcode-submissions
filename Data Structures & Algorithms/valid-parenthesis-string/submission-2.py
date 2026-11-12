from functools import lru_cache

class Solution:
    def checkValidString(self, s: str) -> bool:
        @lru_cache(maxsize=None)
        def helper(i, left):
            if left < 0:
                return False
            if i == len(s):
                return left == 0
            if s[i] == '(':
                return helper(i+1, left+1)
            if s[i] == ')':
                return helper(i+1, left-1)
            else:
                return helper(i+1, left) or helper(i+1, left+1) or helper(i+1, left-1)
        return helper(0, 0)
                