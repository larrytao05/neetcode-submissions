class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        if nums[0] + nums[1] + nums[2] > 0:
            return []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if cur < 0:
                    l += 1
                elif cur > 0:
                    r -= 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return res