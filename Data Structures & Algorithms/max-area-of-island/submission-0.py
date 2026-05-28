class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        maxArea = 0
        def bfs(x,y):
            q = deque()
            q.append((x,y))
            grid[x][y] = 0
            area = 1
            while q:
                i,j = q.popleft()
                for d in dirs:
                    new_x,new_y = i+d[0],j+d[1]
                    if new_x >= 0 and new_y >= 0 and new_x < len(grid) and new_y < len(grid[0]):
                        if grid[new_x][new_y] == 1:
                            q.append((new_x,new_y))
                            grid[new_x][new_y] = 0
                            area+=1
            return area
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, bfs(i,j))
        return maxArea
