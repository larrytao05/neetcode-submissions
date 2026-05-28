class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def helper(i, acc):
            res.append(acc[:])
            if i == len(nums):
                return
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                acc.append(nums[j])
                helper(j+1, acc)
                acc.pop()
        helper(0, [])
        return res
            

            