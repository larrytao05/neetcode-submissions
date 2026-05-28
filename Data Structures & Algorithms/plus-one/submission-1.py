class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            curDig = digits[i]
            if carry > 0:
                curDig += carry
                carry = 0
            if curDig >= 10: 
                digits[i] = (curDig) % 10
                carry = 1
            else:
                digits[i] = curDig
        if carry > 0:
            digits.insert(0, carry)
        return digits
