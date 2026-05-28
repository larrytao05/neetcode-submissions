class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {2:{'A','B','C'},3:{'D','E','F'},4:{'G','H','I'},
        5:{'J','K','L'},6:{'M','N','O'},7:{'P','Q','R','S'},8:{'T','U','V'},
        9:{'W','X','Y','Z'}}
        res = []
        def dfs(i, acc):
            if i == len(digits):
                if len(acc) > 0:
                    res.append("".join(acc[:]))
                return
            for val in letters[int(digits[i])]:
                acc.append(val.lower())
                dfs(i+1,acc)
                acc.pop()
        dfs(0,[])
        return res