class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = 0
        stack = []

        for i in range(len(heights) + 1):
            cur = 0 if i == len(heights) else heights[i]

            while stack and heights[stack[-1]] > cur:

                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                
                best = max(best, width * h)
            stack.append(i)
            
        return best