class MinStack:

    def __init__(self):
        self.stack = []
        self.min = -float("inf")
        self.dic = {}

    def push(self, a):
        self.stack.append(a)
        if a < self.min:
            self.dic[a] = self.min
            self.min = a

    def pop(self):
        if self.stack[-1] != self.min:
            res = self.stack.pop()
            return res
        else:
            self.min = self.dic[self.min]
            res = self.stack.pop()
            del (self.dic[res])
            return res

    def retrieve(self):
        return self.stack[-1]

