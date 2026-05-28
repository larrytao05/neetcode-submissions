class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        m = len(grid)
        n = len(grid[0])
        def bfs(x,y):
            visited = {(x,y)}
            q = deque()
            q.append((x,y,0))
            closest = 2147483647
            while q:
                x,y,dist = q.popleft()
                if grid[x][y] == 0:
                    closest = min(closest, dist)
                    continue
                for i,j in dirs:
                    new_x,new_y = x+i,y+j
                    if new_x >= 0 and new_y >= 0 and new_x < m and new_y < n and grid[new_x][new_y] != -1 and (new_x,new_y) not in visited:
                        q.append((new_x,new_y,dist+1))
                        visited.add((new_x,new_y))
            return closest
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2147483647:
                    grid[i][j] = bfs(i,j)