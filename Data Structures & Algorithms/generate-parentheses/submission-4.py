class Solution:
    def __init__(self):
        self.res = []

    def generateParenthesis(self, n: int) -> List[str]:
        def generate(n, op, acc):
            if n == 0 and op == 0:
                self.res.append(acc)
                return
            elif op > n or op < 0:
                return
            n-=1
            generate(n, op+1,acc+"(")
            generate(n,op-1,acc+")")
        generate(2*n, 0, "")
        return self.res
