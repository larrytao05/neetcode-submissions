class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        numJumps = 0
        for i in range(len(nums)):
            if farthest >= len(nums)-1:
                return numJumps
            if i + nums[i] > farthest:
                farthest = i + nums[i]
                numJumps += 1
        return numJumps