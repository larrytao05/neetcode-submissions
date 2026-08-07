class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        m = len(board)
        n = len(board[0])
        def dfs(i,j, x):
            if x == len(word):
                return True
            if not (0 <= i < m) or not(0 <= j < n) or not (word[x] == board[i][j]):
                return False
            tmp = board[i][j]
            board[i][j] = '#'
            for dr,dc in dirs:
                nr,nc = i+dr,j+dc
                if dfs(nr,nc,x+1):
                    return True
            board[i][j] = tmp
        
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False
                
            