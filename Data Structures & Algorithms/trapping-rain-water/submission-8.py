class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = rightMax = -1
        l = 0
        r = len(height) - 1
        res = 0

        while l <= r:
            left = height[l]
            right = height[r]
            if left >= leftMax:
                leftMax = left
                l += 1
            elif right >= rightMax:
                rightMax = right
                r -= 1
            elif leftMax > rightMax:
                res += rightMax - right
                r -= 1
            else:
                res += leftMax - left
                l += 1
            
        return res