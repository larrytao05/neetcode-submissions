class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(i, acc, currSum):
            if currSum == target:
                res.append(acc.copy())
                return
            for j in range(i+1, len(candidates)):
                if j > (i+1) and candidates[j] == candidates[j-1]:
                    continue
                if currSum + candidates[j] > target:
                    return
                acc.append(candidates[j])
                helper(j, acc, currSum + candidates[j])
                acc.pop()
        helper(-1, [], 0)
        return res
            