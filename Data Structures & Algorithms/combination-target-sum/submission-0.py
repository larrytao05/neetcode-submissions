class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(i, acc, currSum):
            if currSum == target:
                res.append(acc.copy())
                return
            if currSum > target or i >= len(nums):
                return
            acc.append(nums[i])
            helper(i, acc, currSum + nums[i])
            acc.pop()
            helper(i+1, acc, currSum)
        helper(0, [], 0)
        return res