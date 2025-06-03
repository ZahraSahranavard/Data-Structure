
#  سوال: برنامه ای بنویسید که 5 لاگ آخر را صف حلقوی چاپ کند.

class Queue:
    def __init__(self, limit=5):
        self.list = [None] * limit
        self.limit = limit
        self.front = -1
        self.rear = -1
        self.log = []

    def insert(self, x):
        if (self.rear + 1) % self.limit == self.front:
            operation = f"Failed to Insert: Queue is full"
            self._update_log(operation)
            return
        if self.rear == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.limit

        self.list[self.rear] = x
        operation = f"Inserted {x} at position {self.rear}"
        self._update_log(operation)
        return

    def delete(self):
        if self.rear == -1:
            # print("Queue is empty")
            operation = "Exception, Failed to delete: Queue is empty"
            self._update_log(operation)
            return
        if self.front == self.rear:  # تک عضوی
            x = self.list[self.front]
            operation = f"Exception, Deleted {x} from position {self.front}"
            self._update_log(operation)
            self.front = -1
            self.rear = -1
            return
        x = self.list[self.front]
        operation = f"Deleted {x} from position {self.front}"
        self._update_log(operation)
        self.front = (self.front + 1) % self.limit
        return

    def show(self):
        if self.front == -1:
            # print("Queue is empty")
            operation = "Showed: Queue is empty"
            self._update_log(operation)
            return

        elements = []
        if self.front > self.rear:
            for i in range(self.front, self.limit):
                elements.append(self.list[i])
                # print(self.list[i])
            for i in range(0, self.rear + 1):
                elements.append(self.list[i])
                # print(self.list[i])
        else:
            for i in range(self.front, self.rear + 1):
                elements.append(self.list[i])
                # print(self.list[i])
        operation = f"Showed queue elements: {elements}"
        self._update_log(operation)

    def is_empty(self):
        res = self.front == -1
        operation = f"Is it empty? {res}"
        self._update_log(operation)
        return

    def is_full(self):
        res = (self.rear + 1) % self.limit == self.front
        operation = f"Is it full? {res}"
        self._update_log(operation)
        return

    def _update_log(self, operation):
        if len(self.log) >= 5:
            self.log.pop(0)
        self.log.append(operation)

    def show_last_operations(self):
        print("Last operations:")
        for op in self.log:
            print(op)


Q1 = Queue()
Q1.insert(100)
Q1.insert(6)
Q1.insert(9)
Q1.delete()
Q1.delete()
Q1.show()
Q1.is_empty()
Q1.is_full()
Q1.show_last_operations()
