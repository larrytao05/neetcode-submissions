class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        res = []
        def helper(i, dots, acc):
            nonlocal res
            if dots == 4 and i == len(s):
                res.append(acc[:-1])
                return
            if dots > 4:
                return
            for j in range(i, min(i+3, len(s))):
                if i != j and s[i] == "0":
                    continue
                if int(s[i:j+1]) < 256:
                    helper(j+1, dots+1, acc + s[i:j+1] + ".")
        helper(0,0,"")
        return res