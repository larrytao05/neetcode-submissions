class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        curr = n
        while curr != 1 and curr not in seen:
            seen.add(curr)
            currSum = 0
            rem = curr % 10
            left = curr // 10
            while left > 0 or rem > 0:
                currSum += rem**2
                rem = left % 10
                left = left // 10
            curr = currSum
            print(currSum)
        print(curr)
        return curr == 1
