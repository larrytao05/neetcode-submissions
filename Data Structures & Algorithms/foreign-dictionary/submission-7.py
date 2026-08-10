from collections import defaultdict, deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        edges = defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}

        for i in range(1, len(words)):
            w1,w2 = words[i-1],words[i]
            idx = 0
            minLen = min(len(w1), len(w2))
            while idx < minLen and w1[idx] == w2[idx]:
                idx += 1
            if idx < minLen:
                edges[w1[idx]].add(w2[idx])
            elif len(w1) > len(w2):
                return ""

        for u in edges:
            for v in edges[u]:
                in_degree[v] += 1
        res = []
        stack = deque([c for c in in_degree if in_degree[c] == 0])
        while stack:
            nxt = stack.pop()
            res.append(nxt)
            for nei in edges[nxt]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    stack.appendleft(nei)
        if len(res) != len(in_degree):
            return ""
        return "".join(res)