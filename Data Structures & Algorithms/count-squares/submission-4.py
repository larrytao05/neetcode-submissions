from collections import defaultdict

class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.pointSet = []

    def add(self, point: List[int]) -> None:
        x,y=point
        self.points[(x,y)] += 1
        self.pointSet.append(point)

    def count(self, point: List[int]) -> int:
        squares = 0
        x,y = point
        for x2,y2 in self.pointSet:
            p1 = (x,y2)
            p2 = (x2,y)
            if (abs(y2 - y) != abs(x2 - x)) or x == x2 or y == y2:
                continue
            squares += self.points[p1] * self.points[p2]
        return squares
        
