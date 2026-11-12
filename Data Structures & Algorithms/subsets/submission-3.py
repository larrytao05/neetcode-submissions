class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def helper(i, acc):
            if i == len(nums):
                result.append(acc)
                return
            new_lst = acc[:]
            helper(i+1, acc)
            new_lst.append(nums[i])
            helper(i+1, new_lst)
        
        helper(0, [])
        return result