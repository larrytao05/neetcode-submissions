class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                out[i] *= nums[j]
        return out