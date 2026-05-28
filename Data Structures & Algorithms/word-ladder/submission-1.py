from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        wordList.append(beginWord)
        if beginWord == endWord or endWord not in wordList:
            return 0
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adj[pattern].append(word)
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return res
                for i in range(len(word)):
                    pattern = cur[:i] + "*" + cur[i+1:]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            res +=1
        return 0