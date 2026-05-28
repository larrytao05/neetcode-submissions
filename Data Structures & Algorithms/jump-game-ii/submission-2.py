class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l=r=0
        while r < len(nums)-1:
            farthest = 0
            i = l
            while i <= r:
                if nums[i] + i > farthest:
                    farthest = nums[i] + i
                i+=1
            l = r + 1
            r = farthest
            jumps += 1
        return jumps