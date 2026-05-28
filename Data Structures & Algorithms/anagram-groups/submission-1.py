class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for st in strs:
            if str(sorted(st)) in res:
                res[str(sorted(st))].append(st)
            else:
                res[str(sorted(st))] = [st]
        finalRes = []
        for k in res.keys():
            v = res[k]
            finalRes.append(v)
        return finalRes