class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        in_deg = [0] * n
        adj_lst = [[] for _ in range(n)]
        for a,b in edges:
            in_deg[b] += 1
            in_deg[a] += 1
            adj_lst[a].append(b)
            adj_lst[b].append(a)

        queue = deque([(0,0)])
        visit = set()
        while queue:
            nxt,par = queue.popleft()
            visit.add(nxt)
            for nei in adj_lst[nxt]:
                if nei in visit and nei != par:
                    return False
                elif nei in visit:
                    continue
                queue.append((nei, nxt))
        return len(visit) == n
        
        