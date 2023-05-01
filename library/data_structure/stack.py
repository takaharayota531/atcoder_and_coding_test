class Stack:
    def __init__(self, size: int):
        self.stack = [None]*size
        self.top = 0

    def push(self, a: int):
        # stackの格納量に余裕がある時
        if self.top < len(self.stack):
            self.stack[self.top] = a
            self.top += 1
            print(self.stack)
        else:
            print('this stack is full')

    def pop(self):
        if 0 < self.top:
            self.top -= 1
            value = self.stack[self.top]
            self.stack[self.top] = None
            return value
        else:
            print('this stack is null')


s = Stack(5)
s.push(8)
s.push(4)
s.push(5)
s.push(6)
a = s.pop()
print(a)
s.push(2)
