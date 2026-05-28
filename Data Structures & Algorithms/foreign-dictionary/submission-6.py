class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        for i in range(1, len(words)):
            minLen = min(len(words[i-1]), len(words[i]))
            if words[i-1][:minLen] == words[i][:minLen] and len(words[i-1]) > len(words[i]):
                return ""
            for j in range(minLen):
                if words[i-1][j] != words[i][j]:
                    adj[words[i-1][j]].add(words[i][j])
                    break
        
        res = []
        visit = {}
        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True

            for n in adj[c]:
                if dfs(n):
                    return True
            
            visit[c] = False
            res.append(c)
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
