'''
Input
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
Output
[null, null, null, null, 5, 5, 1, 5, 1, 5]
'''

class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        # check if max stack
        if not self.maxStack:
            self.maxStack.append(x)
        else:
            self.maxStack.append(max(x, self.maxStack[-1]))

    def pop(self) -> int:
        self.maxStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.maxStack[-1]

    def popMax(self) -> int:
        tmp = []
        # find the max value in stack which = value in max stack
        while self.stack[-1] != self.maxStack[-1]:
            tmp.append(self.stack.pop())
            self.maxStack.pop()
        ans = self.stack.pop()
        self.maxStack.pop()
        # add values in tmp back to stack
        while tmp:
            val = tmp.pop()
            self.stack.append(val)
            # if maxStack is already empty or not
            if not self.maxStack:
                self.maxStack.append(val)
            else:
                self.maxStack.append(max(val, self.maxStack[-1]))
        return ans
