class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret = []
        def helper(res, lst, i):
            if res == target:
                ret.append(lst[::])
                return
            if i >= len(candidates) or res > target:
                return
            c = candidates[i]
            lst.append(c)
            helper(res+c, lst, i+1)
            lst.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            helper(res, lst, i+1)
        helper(0, [], 0)
        return ret
