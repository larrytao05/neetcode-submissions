from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(set)
        wordList.append(beginWord)
        for word in wordList:
            for other in wordList:
                if word == other:
                    continue
                diff = 0
                for i in range(len(beginWord)):
                    if word[i] != other[i]:
                        diff+=1
                    if diff > 1:
                        break
                if diff == 1:
                    adj[word].add(other)
                    adj[other].add(word)
        visited = set()
        q = deque([(beginWord,1)])
        while q:
            cur,dis = q.popleft()
            if cur == endWord:
                return dis
            for nxt in adj[cur]:
                if nxt not in visited:
                    q.append((nxt, dis+1))
                    visited.add(nxt)
        return 0