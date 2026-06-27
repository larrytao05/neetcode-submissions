class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        while l <= r:
            mdpt = (r+l)//2
            if matrix[mdpt][0] > target:
                r = mdpt - 1
            elif matrix[mdpt][-1] < target:
                l = mdpt + 1
            else:
                i = 0
                j = len(matrix[mdpt])-1
                while i <= j:
                    md = (i+j)//2
                    if matrix[mdpt][md] > target:
                        j = md - 1
                    elif matrix[mdpt][md] < target:
                        i = md + 1
                    else:
                        return True
                return False
        return False