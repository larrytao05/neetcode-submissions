class Solution:
    def hammingWeight(self, n: int) -> int:
        numOnes = 0
        while n:
            if n & 1:
                numOnes += 1
            n = n >> 1
        return numOnes