class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for item in strs:
            res += str(len(item)) + "#" + item
        return res
    def decode(self, s: str) -> List[str]:
        cur = 0
        res = []
        while cur < len(s):
            l = cur
            while s[l] != "#":
                l += 1
            sz = int(s[cur:l])
            nxt = s[l+1:l+1+sz]
            res.append(nxt)
            cur = l+1+sz
        return res