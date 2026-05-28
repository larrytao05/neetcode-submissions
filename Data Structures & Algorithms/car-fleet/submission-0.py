class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        numFleets = 1
        stack = []
        n = len(position)
        adj = sorted(zip(position,speed))
        for i in range(n-1, -1, -1):
            arrival = (target-adj[i][0])/adj[i][1]
            if not stack:
                stack.append((adj[i][0], arrival))
            else:
                if stack[-1][1] < arrival and stack[-1][0] > adj[i][0]:
                    while stack:
                        stack.pop()
                    numFleets += 1
                    stack.append((adj[i][0], arrival))
                else:
                    stack.append((adj[i][0],max(arrival, stack[-1][1])))
        return numFleets
