class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        digToC = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []
        def backtrack(i, acc):
            if i == len(digits):
                res.append(''.join(acc))
                return
            d = digits[i]
            for c in digToC[d]:
                new_acc = acc[:]
                new_acc.append(c)
                backtrack(i+1, new_acc)
        backtrack(0, [])
        return res