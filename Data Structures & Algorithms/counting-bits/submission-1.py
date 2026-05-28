class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        cur = 1
        for i in range(1,n+1):
            if cur * 2 == i:
                cur = i
            res[i] = res[i-cur] + 1
        return res