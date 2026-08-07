class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(starting):
            dirs = [[1,0], [0,1], [-1,0], [0,-1]]
            m = len(heights)
            n = len(heights[0])
            seen = set()
            for x in starting:
                seen.add(x)
            while starting:
                r,c = starting.pop()
                seen.add((r,c))
                for dr,dc in dirs:
                    nr, nc = dr+r,dc+c
                    if 0 <= nr < m and 0 <= nc < n and (nr,nc) not in seen and heights[nr][nc] >= heights[r][c]:
                        starting.append((nr,nc))
                        seen.add((nr,nc))
            return seen
        pac = []
        for i in range(len(heights)):
            pac.append((i,0))
        for j in range(1,len(heights[0])):
            pac.append((0,j))

        v1 = bfs(pac)
        
        atl = []
        for i in range(len(heights)):
            atl.append((i,len(heights[0])-1))
        for j in range(len(heights[0])):
            atl.append((len(heights)-1,j))
        
        v2 = bfs(atl)

        res = []
        for r,c in v1:
            if (r,c) in v2:
                res.append([r,c])
        return res

