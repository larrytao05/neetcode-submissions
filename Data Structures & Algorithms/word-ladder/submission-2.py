from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        edges = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                edges[word[:i] + "*" + word[i+1:]].append(word)
        
        q = deque()
        q.append(beginWord)
        seen = set()
        cost = {beginWord: 1}
        while q:
            nxt = q.pop()
            if nxt == endWord:
                return cost[endWord]
            for i in range(len(nxt)):
                key = nxt[:i] + "*" + nxt[i+1:]
                for nei in edges[key]:
                    if nei in cost:
                        continue
                    cost[nei] = cost[nxt] + 1
                    q.appendleft(nei)
        
        return 0
        
