class Queue:
    def __init__(self, limit=10):
        self.list = [None] * limit
        self.limit = limit
        self.front = -1
        self.rear = -1

    def enqueue(self,x):   #insert
        if (self.rear+1) % self.limit == self.front:
            print("Queue is full")
            return
        if self.rear == -1:
            self.front += 1
            self.rear += 1
            self.list[0] = x
            return
        self.list[(self.rear + 1) % self.limit] = x
        self.rear = (self.rear + 1) % self.limit

    def delete(self):
        if self.rear == -1:
            print("Queue is empty")
            return
        if self.front == self.rear:
            x = self.list[self.front]
            self.front = -1
            self.rear = -1
            return x
        x = self.list[self.front]
        self.front = (self.front + 1) % self.limit
        return x

    def show(self):
        if self.front == -1:
            print("Queue is empty")
            return
        if self.front > self.rear:
            for i in range(self.front, self.limit):
                print(self.list[i])
            for i in range(0, self.rear + 1):
                print(self.list[i])
        for i in range (self.front, self.rear + 1):
            print(self.list[i])

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.limit == self.front



        