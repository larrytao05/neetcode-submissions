class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}
        for i in range(3):
            for j in range(3):
                boxes[(i,j)] = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                val = board[i][j]
                

                if val in rows[i]:
                    return False
                if val in cols[j]:
                    return False
                if val in boxes[(i//3,j//3)]:
                    
                    return False
                rows[i].add(val)
                cols[j].add(val)
                boxes[(i//3,j//3)].add(val)
        
        return True
                