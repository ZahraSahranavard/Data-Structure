class Queue:

    def __init__(self, limit=10):
        self.list = [None] * limit
        self.limit = limit
        self.front = -1
        self.rear = -1

    def enqueue(self,x):   #insert
        if self.rear >= self.limit - 1:
            print("Queue is full")
            return
        self.rear += 1
        self.list[self.rear] = x
        if self.front == -1:
            self.front += 1

    def dequeue(self):   #delete
        if(self.front > self.rear) or (self.front == -1):
            print("Queue is empty")
            return
        self.front += 1
        return self.list[self.front - 1]

    def show(self):
        if (self.front > self.rear) or (self.front == -1):
            print("Queue is empty")
            return
        for i in range(self.front, self.rear + 1):
            print(self.list[i])

    def is_full(self):
        return self.rear >= self.limit - 1

    def is_empty(self):
        return self.front > self.rear


# Test
q = Queue()
q.enqueue(0)
q.enqueue(40)
q.enqueue(10)
q.enqueue(24)
q.enqueue(37)
q.enqueue(100)
q.dequeue()
q.show()
