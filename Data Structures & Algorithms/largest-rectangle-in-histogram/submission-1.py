class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxA = 0
        for i in range(n+1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                ind = stack.pop()
                height = heights[ind]
                width = i if not stack else i-stack[-1]-1
                maxA = max(maxA, height * width)
            stack.append(i)
        return maxA
                
