class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0
        def dfs(r,c):
            if not (0 <= r < m) or not (0 <= c < n) or not grid[r][c] == '1':
                return
            grid[r][c] = '0'
            for dr,dc in [[1,0], [0,1], [-1,0], [0,-1]]:
                nr,nc = r+dr,c+dc
                dfs(nr,nc)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i,j)
        return islands
