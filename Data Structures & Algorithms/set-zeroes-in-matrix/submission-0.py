class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for x in range(m):
                        if matrix[x][j] != 0:
                            matrix[x][j] = "*"
                    for y in range(n):
                        if matrix[i][y] != 0:
                            matrix[i][y] = "*"
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "*":
                    matrix[i][j] = 0
        