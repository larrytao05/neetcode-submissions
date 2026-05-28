class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            sort = ''.join(sorted(s))
            anagrams[sort].append(s)
        return list(anagrams.values())