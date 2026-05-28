from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)


        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                b_x, b_y = i // 3, j // 3
                if board[i][j] in boxes[(b_x,b_y)]:
                    return False
                boxes[(b_x,b_y)].add(board[i][j])
                if board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])
                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])
        return True
