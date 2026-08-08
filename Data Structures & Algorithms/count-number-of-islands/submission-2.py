class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0
        def dfs(r,c):
            grid[r][c] = '0'
            for dr,dc in [[1,0], [0,1], [-1,0], [0,-1]]:
                nr,nc = r+dr,c+dc
                if (0 <= nr < m) and (0 <= nc < n) and grid[nr][nc] == '1':
                    dfs(nr,nc)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i,j)
        return islands
