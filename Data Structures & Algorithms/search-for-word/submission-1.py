class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visiting = [[False]  * len(board[0]) for _ in range(len(board))]
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        def dfs(r,c, ind):
            if not (0 <= r < len(board) and 0 <= c < len(board[0])):
                return False
            print(board[r][c])
            if visiting[r][c]:
                return False
            if board[r][c] == word[ind]:
                ind += 1
            else:
                return False
            if ind == len(word):
                return True
            visiting[r][c] = True
            for dr,dc in dirs:
                if dfs(r+dr,c+dc,ind):
                    return True
            visiting[r][c] = False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0):
                    return True
        return False

