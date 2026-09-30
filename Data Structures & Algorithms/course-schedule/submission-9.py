class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * numCourses
        adj = defaultdict(list)
        for a,b in prerequisites:
            adj[b].append(a)
            inDegree[a] += 1
        
        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        
        visit = 0
        while queue:
            nxt = queue.popleft()
            visit += 1
            for nei in adj[nxt]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    queue.append(nei)
        
        return visit == numCourses