from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()
        for s,e in tickets:
            adj[s].append(e)
        res = ["JFK"]
        def dfs(start):
            if len(res) == len(tickets) + 1:
                return True
            if start not in adj:
                return False
            temp = adj[start]
            for i,nei in enumerate(temp):
                adj[start].pop(i)
                res.append(nei)
                if dfs(nei):
                    return True
                adj[start].insert(i, nei)
                res.pop()
        dfs("JFK")
        return res