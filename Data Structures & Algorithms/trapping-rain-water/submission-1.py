class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        leftMax = height[l]
        rightMax = height[r]
        trapped = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                if leftMax < height[l]:
                    leftMax = height[l]
                trapped += leftMax - height[l]
            else:
                r -= 1
                if rightMax < height[r]:
                    rightMax = height[r]
                trapped += rightMax - height[r]
        return trapped