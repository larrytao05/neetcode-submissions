from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        edges = {c:set() for w in words for c in w}
        chars = set()
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            minLen = min(len(word1),len(word2))
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            for j in range(minLen):
                if word1[j] != word2[j]:           
                    edges[word1[j]].add(word2[j])
                    break
        visit = {}
        res = []
        
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in edges[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
        for c in edges:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
        
            