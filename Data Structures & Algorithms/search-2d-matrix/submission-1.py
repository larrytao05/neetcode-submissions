class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # row-wise and then column-wise
        def helper(l,r, row):
            if r-l<2:
                if matrix[row][l] == target:
                    return True
                else:
                    return False
            mid = (r+l)//2
            if target < matrix[row][mid]:
                return helper(l,mid,row)
            else:
                return helper(mid,r,row)
        def row_helper(l,r):
            if r-l<2:
                if matrix[l][0] <= target and matrix[l][-1] >= target:
                    return l
                else:
                    return -1
            mid = (r+l)//2
            if target < matrix[mid][0]:
                return row_helper(l,mid)
            else:
                return row_helper(mid,r)
        m = len(matrix)
        n = len(matrix[0])
        row = row_helper(0,m)
        if row == -1:
            return False
        return helper(0,n,row)