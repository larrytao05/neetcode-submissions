class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = math.inf

    def push(self, val: int) -> None:
        if self.minVal <= val:
            self.stack.append((val, self.minVal))
        else:
            self.stack.append((val, val))
            self.minVal = val

    def pop(self) -> None:
        val,thisMin = self.stack.pop()
        if self.stack:
            self.minVal = self.stack[-1][1]
        else:
            self.minVal = math.inf


    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.minVal

