import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minH = [(grid[0][0], 0, 0)]
        visit = set()
        visit.add((0,0))
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        while minH:
            t,x,y = heapq.heappop(minH)
            if x == n-1 and y == n-1:
                return t
            for dx,dy in dirs:
                new_x,new_y = x+dx,y+dy
                if (0 <= new_x < n) and (0 <= new_y < n) and (new_x,new_y) not in visit:
                    visit.add((new_x,new_y))
                    heapq.heappush(minH, [max(t,grid[new_x][new_y]), new_x,new_y])
        