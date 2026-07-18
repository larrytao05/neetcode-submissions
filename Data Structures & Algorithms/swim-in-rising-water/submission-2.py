class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        n = len(grid)
        target = (n-1,n-1)
        q = [(grid[0][0],0,0)]
        h = 0

        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        while target not in visited:
            w,x,y = heapq.heappop(q)
            if h < w:
                h = w
            visited.add((x,y))
            for dx,dy in dirs:
                n_x,n_y = dx + x, dy + y
                if 0 <= n_x < n and 0 <= n_y < n and (n_x,n_y) not in visited:
                    heapq.heappush(q, (grid[n_x][n_y], n_x,n_y))
        return h
