class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i, acc):
            nonlocal res
            if i == len(nums)-1:
                res.append(acc)
                res.append(acc + [nums[i]])
                return
            helper(i+1, acc)
            helper(i+1, acc + [nums[i]])
        helper(0, [])
        return res
