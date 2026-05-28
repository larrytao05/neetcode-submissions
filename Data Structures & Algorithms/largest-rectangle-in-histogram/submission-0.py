class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        leftBounds = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftBounds[i] = stack[-1]
            stack.append(i)
        
        stack = []
        rightBounds = [n] * n
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightBounds[i] = stack[-1]
            stack.append(i)
        
        res = 0
        for i in range(n):
            leftBounds[i] += 1
            rightBounds[i] -= 1
            area = (rightBounds[i]-leftBounds[i]+1) * heights[i]
            res = max(area, res)
        return res