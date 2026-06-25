class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = []
        n = len(position)
        comb = [(position[i], speed[i]) for i in range(len(position))]
        comb.sort()
        for i in range(n-1, -1, -1):
            t_2 = (target-comb[i][0])/comb[i][1]
            if s:
                j = s[-1]
                t_1 = (target-comb[j][0])/comb[j][1]
                if t_2 > t_1:
                    s.append(i)
            else:
                s.append(i)
        return len(s)
        