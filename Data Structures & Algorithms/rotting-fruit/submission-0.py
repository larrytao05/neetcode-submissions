from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        m = len(grid)
        n = len(grid[0])
        def bfs(starts, count):
            q = deque()
            for x,y in starts:
                q.append((x,y,0))
            minutes = 0
            freshLeft = count
            while q:
                x,y,curMin = q.popleft()
                minutes = max(minutes, curMin)
                for i,j in dirs:
                    new_x,new_y = x+i,y+j
                    if new_x >= 0 and new_y >= 0 and new_x < m and new_y < n and grid[new_x][new_y] == 1:
                        q.append((new_x,new_y,curMin+1))
                        grid[new_x][new_y] = 2
                        freshLeft -= 1
            return (minutes, freshLeft)
        starts = []
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    starts.append((i,j))
                elif grid[i][j] == 1:
                    count += 1
        time,rem = bfs(starts, count)
        return time if rem == 0 else -1

