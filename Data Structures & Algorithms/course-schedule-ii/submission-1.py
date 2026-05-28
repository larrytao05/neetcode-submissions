class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        taken = set()
        prereqs = defaultdict(set)
        frees = defaultdict(set)
        order = []
        for a,b in prerequisites:
            prereqs[a].add(b)
            frees[b].add(a)
        if len(prereqs) == numCourses:
            return []
        def bfs(a):
            taken.add(a)
            order.append(a)
            q = deque()
            q.append(a)
            while q:
                nxt = q.popleft()
                for free in frees[nxt]:
                    if free not in taken and len(prereqs[free]) == 1:
                        q.append(free)
                        taken.add(free)
                        order.append(free)
                    prereqs[free].remove(nxt)
        for i in range(numCourses):
            if i not in prereqs and i not in taken: 
                bfs(i)
        if len(taken) == numCourses:
            return order
        return []