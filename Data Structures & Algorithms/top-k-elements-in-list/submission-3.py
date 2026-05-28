class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def func(item):
            return item[1]
        counts = sorted(Counter(nums).items(), key=func, reverse=True)
        res = []
        for i in range(k):
            k,v = counts[i]
            res.append(k)
        return res
