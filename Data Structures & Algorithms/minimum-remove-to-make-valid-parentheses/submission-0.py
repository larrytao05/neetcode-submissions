class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        count = 0
        for c in s:
            if c == '(':
                count += 1
                res.append(c)
            elif c == ')':
                if count > 0:
                    res.append(c)
                    count -= 1
            else:
                res.append(c)
            
        final = []
        for i in range(len(res)-1, -1, -1):
            c = res[i]
            if c == '(' and count > 0:
                count -= 1
                continue
            else:
                final.append(c)
        return "".join(final[::-1])