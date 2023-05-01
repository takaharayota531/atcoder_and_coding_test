class Queue:
    def __init__(self, size: int):
        self.queue = [None]*size
        self.head = 0
        self.tail = 0

    def enqueue(self, value: int):
        if self.tail < len(self.queue):
            self.queue[self.tail] = value
            self.tail += 1
            print(self.queue)

        else:
            print('this queue is full')

    def dequeue(self):
        if self.head < self.tail:
            value = self.queue[self.head]
            self.queue[self.head] = None
            self.head += 1
            print(self.queue)
            return value

        else:
            print('this queue is empty')


q = Queue(5)
q.enqueue(8)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
a = q.dequeue()
print(a)
q.enqueue(2)
b = q.dequeue()
print(b)
