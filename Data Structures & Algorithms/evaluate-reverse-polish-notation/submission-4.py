class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        ops = set(['+','-','*','/'])
        for token in tokens:
            if token not in ops:
                s.append(int(token))
            else:
                x,y = s.pop(),s.pop()
                if token == '+':
                    s.append(x+y)
                elif token == '-':
                    s.append(y-x)
                elif token == '*':
                    s.append(y*x)
                else:
                    s.append(int(y/x))
                print(s[-1])
        return s[0]