class MinStack:

    def __init__(self):
        self.stk = deque()
        self.mini = []
    def push(self, val: int) -> None:
        self.stk.append(val)
        val = min(val, self.mini[-1] if self.mini else val)
        self.mini.append(val)

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return min(self.stk)
