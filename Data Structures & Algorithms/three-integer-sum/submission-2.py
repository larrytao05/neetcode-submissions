class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0
        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            if a > 0:
                return res
            l,r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == -a:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                elif nums[l] + nums[r] + a > 0:
                    r-=1
                else:
                    l+=1
        return res
            


