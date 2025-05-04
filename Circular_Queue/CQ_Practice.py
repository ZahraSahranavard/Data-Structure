
#  سوال: برنامه ای بنویسید که 5 لاگ آخر را صف حلقوی چاپ کند.

from datetime import datetime
import time
def log_exceptions(method):
    def wrapper(self, *args, **kwargs):
        try:
            return method(self, *args, **kwargs)
        except Exception as e:
            error_message = f"Error in {method.__name__}: {str(e)}"
            print(error_message)
            self._update_log(error_message)
    return wrapper

class CircularLogQueue:
    def __init__(self, size=5):
        self.size = size
        self.logs = [None] * size
        self.front = 0
        self.count = 0

    def add(self, item):
        index = (self.front + self.count) % self.size
        self.logs[index] = f"[{datetime.now().strftime('%H:%M:%S')}] {item}"
        if self.count < self.size:
            self.count += 1
        else:
            self.front = (self.front + 1) % self.size

    def get_logs(self):
        result = []
        for i in range(self.count):
            index = (self.front + i) % self.size
            result.append(self.logs[index])
        return result[::-1]
    def get_logs(self):
        result = []
        for i in range(self.count):
            index = (self.front + i) % self.size
            result.append(self.logs[index])
        return result[::-1]

class Queue:
    def __init__(self, limit=5):
        self.list = [None] * limit
        self.limit = limit
        self.front = -1
        self.rear = -1
        self.log = CircularLogQueue()

    @log_exceptions
    def insert(self, x):
        if (self.rear + 1) % self.limit == self.front:
            # print("Queue is full")
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

    @log_exceptions
    def delete(self):
        if self.rear == -1:
            # print("Queue is empty")
            operation = "Exception, Failed to delete: Queue is empty"
            self._update_log(operation)
            return
        if self.front == self.rear:
            x = self.list[self.front]
            operation = f"Exception, Deleted {x} from position {self.front}"
            self._update_log(operation)
            self.front = -1
            self.rear = -1
            return x
        x = self.list[self.front]
        operation = f"Deleted {x} from position {self.front}"
        self._update_log(operation)
        self.front = (self.front + 1) % self.limit
        return x

    @log_exceptions
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

    @log_exceptions
    def is_empty(self):
        res = self.front == -1
        operation = f"Is it empty? {res} "
        self._update_log(operation)
        return res

    @log_exceptions
    def is_full(self):
        res = (self.rear + 1) % self.limit == self.front
        operation = f"Is it full? {res} "
        self._update_log(operation)
        return res

    def _update_log(self, operation):
        self.log.add(operation)

    @log_exceptions
    def show_last_operations(self):
        print("Last operations:")
        for op in self.log.get_logs():
            print(op)



Q1 = Queue()
Q1.insert(100)
time.sleep(1)
Q1.insert(6)
time.sleep(1)
Q1.insert(9)
time.sleep(1)
Q1.delete()
time.sleep(1)
Q1.delete()
time.sleep(1)
Q1.insert(60)
Q1.insert(11)
Q1.insert(78)
Q1.show()
time.sleep(1)
Q1.is_empty()
Q1.insert(12)
Q1.insert(1)
Q1.insert(7)
Q1.is_full()
Q1.show_last_operations()
