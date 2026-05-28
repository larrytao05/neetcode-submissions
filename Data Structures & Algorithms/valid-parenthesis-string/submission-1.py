class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack = []
        star = []
        for i,c in enumerate(s):
            if c == '(':
                leftStack.append(i)
            elif c == '*':
                star.append(i)
            else:
                if len(leftStack) > 0:
                    leftStack.pop()
                elif len(star) > 0:
                    star.pop()
                else:
                    return False
        while leftStack and star:
            if star.pop() < leftStack.pop():
                return False
        return not leftStack