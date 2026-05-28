class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        n = len(nums)
        out = [1] * n
        for i in range(1,n):
            pre *= nums[i-1]
            out[i] = pre

        post = 1
        for j in range(n-2, -1,-1):
            post *= nums[j+1]
            out[j] *= post
        return out