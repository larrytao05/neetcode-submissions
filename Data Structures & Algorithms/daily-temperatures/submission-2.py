class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        
        stack = []
        res = [0] * n
        
        for i,t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                j,t_0 = stack.pop()
                res[j] = i-j
            stack.append((i,t))
        
        return res