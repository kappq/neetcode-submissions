class MinStack:
    st: list[int]
    mono: list[int]

    def __init__(self):
        self.st = []
        self.mono = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if len(self.mono) == 0 or val <= self.mono[-1]:
            self.mono.append(val)

    def pop(self) -> None:
        val = self.st.pop()
        if self.mono[-1] == val:
            self.mono.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mono[-1]
