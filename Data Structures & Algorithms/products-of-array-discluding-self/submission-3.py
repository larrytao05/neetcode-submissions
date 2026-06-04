class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        numZeros = 0
        for n in nums:
            if n == 0:
                numZeros += 1
                continue
            total *= n

        output = []
        for n in nums:
            if n == 0 and numZeros > 1:
                output.append(0)
            elif n == 0:
                output.append(total)
            elif numZeros > 0:
                output.append(0)
            else:
                output.append(total // n)
        
        return output
        