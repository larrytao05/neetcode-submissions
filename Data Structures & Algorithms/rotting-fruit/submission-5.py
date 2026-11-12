class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        numOranges = 0
        queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    numOranges += 1
                if grid[i][j] == 2:
                    queue.append((i,j))
                

        if numOranges == 0:
            return 0

        timeElapsed = 0
        while queue and numOranges > 0:
            for i in range(len(queue)):
                x,y = queue.popleft()
                for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        queue.append((nx,ny))
                        grid[nx][ny] = 2
                        numOranges -= 1
            
            timeElapsed += 1
            if numOranges == 0:
                return timeElapsed
                    
        
        if numOranges == 0:
            return timeElapsed
        return -1
