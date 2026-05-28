class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(x,y, ind):
            if ind == len(word):
                return True
            if (x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[ind] or board[x][y] == '#'):
                return False
            board[x][y] = '#'
            res = (helper(x+1,y,ind+1) or helper(x,y+1,ind+1) or helper(x-1,y,ind+1) or helper(x,y-1,ind+1))
            board[x][y] = word[ind]
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i,j,0):
                    return True
        return False