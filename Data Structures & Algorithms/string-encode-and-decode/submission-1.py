class Solution:
    encodings = dict()
    nextkey = 0
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for item in strs:
            self.encodings[str(self.nextkey)] = item
            encoded.append(str(self.nextkey) + " ")
            self.nextkey += 1
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        res = []
        for c in s.split():
            res.append(self.encodings[c])
        return res