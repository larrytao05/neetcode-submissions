class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(['*', '+', '/', '-'])

        for t in tokens:
            if t in ops:
                x = stack.pop()
                y = stack.pop()
                res = None
                if t == '*':
                    res = x * y
                elif t == '+':
                    res = x + y
                elif t == '/':
                    if y < 0 or x < 0:
                        y *= -1
                        res = (y // x) * -1
                    else:
                        res = y // x
                else:
                    res = y - x
                stack.append(int(res))
            else:
                stack.append(int(t))
        return stack[-1]
