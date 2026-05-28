class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]
        rows = set()
        posDiag = set()
        negDiag = set()    
        def helper(y):
            if y == n:
                res.append(["".join(row) for row in board.copy()])
                return
            for i in range(n):
                if i in rows or (i+y) in posDiag or (i-y) in negDiag:
                    continue
                board[y][i] = "Q"
                rows.add(i)
                posDiag.add(i+y)
                negDiag.add(i-y)
                helper(y+1)
                board[y][i] = "."
                rows.remove(i)
                posDiag.remove(i+y)
                negDiag.remove(i-y)
        helper(0)
        return res
