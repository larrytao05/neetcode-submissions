class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            cur = temperatures[i]
            while s and s[-1][0] < cur:
                _,ind = s.pop()
                res[ind] = i-ind
            s.append((cur, i))
        return res