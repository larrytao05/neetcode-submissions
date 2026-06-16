class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftMax = rightMax = -1
        l = 0
        r = len(heights) - 1
        res = 0

        while l <= r:
            height = min(heights[l], heights[r])
            width = r-l
            res = max(res, height * width)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res

