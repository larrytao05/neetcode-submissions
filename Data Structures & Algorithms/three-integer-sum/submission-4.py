class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        trips = []
        for i in range(len(nums)):
            if i and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                return trips
            l = i+1
            r = len(nums)-1
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    trips.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return trips