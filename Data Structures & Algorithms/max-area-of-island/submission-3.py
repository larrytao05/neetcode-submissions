class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def traverseIsland(x, y):
            grid[x][y] = 0
            area = 1
            for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    area += traverseIsland(nx, ny)
            return area

        best = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = traverseIsland(i, j)
                    best = max(best, area)
        return best
            