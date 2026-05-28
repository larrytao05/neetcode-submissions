class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        dic = {}
        for a,b in prerequisites:
            if b in dic:
                dic[b].append(a)
            else:
                dic[b] = [a]

        seen = set()
        visiting = set()

        def dfs(start):
            if start in visiting:
                return False
            if start in seen:
                return True
            visiting.add(start)
            if start in dic:
                for nei in dic[start]:
                    if dfs(nei) == False:
                        return False
            visiting.remove(start)
            seen.add(start)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True
            