from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = [[set() for _ in range(9)] for _ in range(9)]

        for r in range(9):
            for c in range(9):
                dig = board[r][c]
                if dig == '.':
                    continue
                if dig in rows[r] or dig in cols[c] or dig in squares[r//3][c //3]:
                    return False
                rows[r].add(dig)
                cols[c].add(dig)
                squares[r//3][c//3].add(dig)
        return True