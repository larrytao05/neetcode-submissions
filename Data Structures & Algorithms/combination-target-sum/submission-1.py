class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def helper(i, acc, currSum):
            if currSum == target:
                res.append(acc.copy())
                return
            for j in range(i, len(nums)):
                if currSum + nums[j] > target:
                    return
                acc.append(nums[j])
                helper(j, acc, currSum + nums[j])
                acc.pop()
        helper(0, [], 0)
        return res