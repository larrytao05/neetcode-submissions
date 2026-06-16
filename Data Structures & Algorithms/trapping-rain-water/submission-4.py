class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = rightMax = -1
        l = 0
        r = len(height) - 1
        res = 0

        while l <= r:
            if height[l] >= leftMax:
                leftMax = height[l]
                l += 1
            elif height[r] >= rightMax:
                rightMax = height[r]
                r -= 1
            elif leftMax > rightMax:
                print("adding " + str(rightMax - height[r]))
                res += rightMax - height[r]
                r -= 1
            else:
                print("adding " + str(rightMax - height[r]))
                res += leftMax - height[l]
                l += 1
            
        return res