class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        max_l,max_r = height[l],height[r]
        total = 0
        while l < r:
            if max_l < max_r:
                l+=1
                max_l = max(height[l],max_l)
                total += max_l - height[l]
            else:
                r-=1
                max_r = max(height[r],max_r)
                total += max_r - height[r]
        return total
                