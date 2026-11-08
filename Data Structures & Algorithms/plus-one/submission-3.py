class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem = 1
        for i in range(len(digits)-1, -1, -1):
            sm = rem + digits[i]
            digits[i] = sm % 10
            rem = sm // 10
        if rem:
            return [rem] + digits
        return digits
            
