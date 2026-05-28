from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        seen = set()
        m  = len(board)
        n = len(board[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        def bfs(x,y):
            q = deque()
            q.append((x,y))
            visited = {(x,y)}
            seen.add((x,y))
            surrounded = True
            while q:
                r,c = q.popleft()
                if r==0 or c==0 or r == m-1 or c == n-1:
                    surrounded = False
                for rd,cd in dirs:
                    new_r,new_c = r+rd,c+cd
                    if (0 <= new_r < m) and (0 <= new_c < n) and board[new_r][new_c] == "O" and (new_r,new_c) not in visited:
                        q.append((new_r,new_c))
                        visited.add((new_r,new_c))
                        seen.add((new_r,new_c))
            if surrounded:
                for i,j in visited:
                    board[i][j] = "X"
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i,j) not in seen:
                    bfs(i,j)
            