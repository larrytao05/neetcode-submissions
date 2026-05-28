from collections import defaultdict,deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        taken = set()
        prereqs = defaultdict(set)
        frees = defaultdict(set)
        for a,b in prerequisites:
            prereqs[a].add(b)
            frees[b].add(a)
        if len(prereqs) == numCourses:
            return False
        def bfs(a):
            taken.add(a)
            q = deque()
            q.append(a)
            print(a)
            print(len(taken))
            while q:
                nxt = q.popleft()
                for free in frees[nxt]:
                    if free not in taken and len(prereqs[free]) == 1:
                        q.append(free)
                        taken.add(free)
                    prereqs[free].remove(nxt)
        for i in range(numCourses):
            if i not in prereqs and i not in taken: 
                bfs(i)
        return len(taken) == numCourses