class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:  
            encoded.append(str(len(s)))
            encoded.append('#')
            encoded.append(s)
        return "".join(encoded)
    def decode(self, s: str) -> List[str]:
        cur = 0
        res = []
        while cur < len(s):
            strLen = ''
            while cur < len(s) and s[cur] != '#':
                strLen += s[cur]
                cur += 1
            cur+=1
            strLen = int(strLen)
            res.append(s[cur:cur+strLen])
            cur = cur+strLen
        return res