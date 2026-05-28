class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def helper(l, r, target):
            if r-l < 2:
                if nums[l] == target:
                    return l
                else:
                    return -1
            mid = (l+r)//2
            if target < nums[mid]:
                return helper(l, mid,target)
            else:
                return helper(mid,r,target)
        return helper(0,n,target)
            

        
