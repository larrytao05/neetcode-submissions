from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights),len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac, atl = set(), set()
        def bfs(source, ocean):
            q = deque(source)
            while q:
                r,c = q.popleft()
                ocean.add((r, c))
                for i,j in directions:
                    new_r,new_c = r+i,c+j
                    if (0 <= new_r < m) and (0 <= new_c < n) and (new_r,new_c) not in ocean and heights[new_r][new_c] >= heights[r][c]:
                        q.append((new_r, new_c))
        pacific = []
        atlantic = []
        for i in range(m):
            pacific.append((i,0))
            atlantic.append((i,n-1))
        for j in range(n):
            pacific.append((0,j))
            atlantic.append((m-1,j))
        bfs(pacific, pac)
        bfs(atlantic,atl)
        res = []
        for r in range(m):
            for c in range(n):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res
