class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minVal = math.inf

    def push(self, val: int) -> None:
        if val < self.minVal:
            self.minVal = val
        self.stack.append((val, self.minVal))

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.minVal = self.stack[-1][1]
        else:
            self.minVal = math.inf

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.minVal
