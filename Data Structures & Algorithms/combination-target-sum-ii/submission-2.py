class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def backtrack(i, cur, acc):
            if cur == target:
                res.append(acc)
            j = i
            while j < len(candidates):
                if cur + candidates[j] <= target:
                    new_acc = acc[:]
                    new_acc.append(candidates[j])
                    backtrack(j+1,cur+candidates[j],new_acc)
                j += 1
                while j < len(candidates) and candidates[j] == candidates[j-1]:
                    j += 1
        backtrack(0, 0, [])

        return res

