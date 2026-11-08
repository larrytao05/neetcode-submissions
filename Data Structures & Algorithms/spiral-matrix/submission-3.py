class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        res = []

        while top <= bottom and left <= right:
            # Left to right across the top row.
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # Top to bottom down the right column.
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # Right to left across the bottom row, if one remains.
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # Bottom to top up the left column, if one remains.
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res