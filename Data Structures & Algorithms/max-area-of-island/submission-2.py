class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cur_area = 0
        def traverseIsland(x, y):
            nonlocal cur_area
            cur_area += 1
            grid[x][y] = 0
            for dx,dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    traverseIsland(nx, ny)

        best = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur_area = 0
                    traverseIsland(i, j)
                    best = max(best, cur_area)
        return best
            