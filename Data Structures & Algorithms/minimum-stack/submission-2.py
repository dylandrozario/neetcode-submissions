class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(len(self.minStack) == 0):
            self.minStack.append(val)
        else:
            val = min(val, self.minStack[-1])
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    

    def top(self) -> int:
        top = self.stack[-1]
        return top

    def getMin(self) -> int:
        top = self.minStack[-1]
        return top
