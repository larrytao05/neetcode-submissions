class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        posDiag = set()
        negDiag = set()
        rows = [False] * n
        # cols = [False] * n
        res = []
        def generateBoard(queens):
            board = []
            for i in range(n):
                j = queens[i]
                board.append('.' * j + 'Q' + '.' * (n-j-1))
            return board

        def backtrack(i, acc):
            if i == n:                              
                res.append(generateBoard(acc))
                return

            for j in range(n):
                if rows[j] or (i+j) in posDiag or (i-j) in negDiag:
                    continue
                new_acc = acc[:]
                new_acc.append(j)
                posDiag.add(i+j)
                negDiag.add(i-j)
                rows[j] = True
                backtrack(i+1, new_acc)
                posDiag.remove(i+j)
                negDiag.remove(i-j)
                rows[j] = False
        backtrack(0, [])
        return res
