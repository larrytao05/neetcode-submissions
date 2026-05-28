class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(acc, picked):
            nonlocal res
            if len(acc) == len(nums):
                res.append(acc[:])
                return
            for i in range(len(nums)):
                if not picked[i]:
                    picked[i] = True
                    acc.append(nums[i])
                    helper(acc, picked)
                    picked[i] = False
                    acc.pop()
        helper([], [False] * len(nums))
        return res
