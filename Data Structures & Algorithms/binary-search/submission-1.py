class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            mdpt = (r+l)//2
            if nums[mdpt] > target:
                r = mdpt-1
            elif nums[mdpt] < target:
                l = mdpt+1
            else:
                return mdpt
        return -1
        