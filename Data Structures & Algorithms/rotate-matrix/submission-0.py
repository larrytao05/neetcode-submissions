class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # row gives column (from end)
        # column gives row
        n = len(matrix)
        l,r = 0,n-1
        while l < r:
            for i in range(r-l):
                top,bottom = l,r
                topLeft = matrix[top][l+i]
                matrix[top][l+i] = matrix[bottom-i][l]
                matrix[bottom-i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = topLeft
            r-=1
            l+=1
                 