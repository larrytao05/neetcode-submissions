class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = {}
        
        maxVal = 0
        def dfs(x,y,prev):
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= prev:
                return 0
            if (x,y) in dp:
                return dp[(x,y)]
            val = matrix[x][y]
            a = dfs(x+1,y,val)
            b = dfs(x,y+1,val)
            c = dfs(x-1,y,val)
            d = dfs(x,y-1,val)
            dp[(x,y)] = max(1+a,1+b,1+c,1+d,1)
            return dp[(x,y)]
        for i in range(m):
            for j in range(n):
                maxVal = max(maxVal, dfs(i,j,-1))
        return maxVal
                