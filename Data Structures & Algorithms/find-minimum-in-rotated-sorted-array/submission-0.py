class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        ret = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                ret = min(ret,nums[l])
                break

            mid = (l+r)//2
            ret = min(ret, nums[mid])
            if nums[mid] < nums[l]:
                r = mid-1
            else:
                l = mid+1
        return ret