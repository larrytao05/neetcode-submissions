class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
    
        def helper(op, closed):
            if op == 0 and closed == 0:
                res.append("".join(stack))
                return
            if op > 0:
                stack.append("(")
                helper(op-1, closed)
                stack.pop()
            if closed > op:
                stack.append(")")
                helper(op, closed-1)
                stack.pop()
        helper(n, n)
        return res
