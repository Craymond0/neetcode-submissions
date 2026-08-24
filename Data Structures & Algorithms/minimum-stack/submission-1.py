class MinStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val: int) -> None:
        self.stack1.append(val)

        if not self.stack2 or val <= self.stack2[-1]:
            self.stack2.append(val)

    def pop(self) -> None:
        if self.stack1[-1] == self.stack2[-1]:
            self.stack2.pop()

        self.stack1.pop() 

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return self.stack2[-1]
