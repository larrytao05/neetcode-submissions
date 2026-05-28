class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cur = 1
        output = []
        for n in nums:
            output.append(cur)
            cur *= n
        cur = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= cur
            cur *= nums[i]
        return output