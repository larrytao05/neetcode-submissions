class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        app = set()
        for n in nums:
            if n in app:
                return True
            app.add(n)
        return False