class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        res = []
        nums.sort()
        def backtrack(i, acc):
            if i == len(nums):
                if tuple(acc) not in seen:
                    res.append(acc)
                    seen.add(tuple(acc))
                return
            backtrack(i+1, acc[:])
            acc.append(nums[i])
            backtrack(i+1,acc)
        
        backtrack(0,[])
        return list(res)

        
            