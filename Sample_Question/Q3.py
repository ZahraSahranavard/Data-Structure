
#     چگونه میتوان یک صف (FIFO) را با استفاده از دو پشته (LIFO) پیاده سازی کرد؟ عملیات enqueue و dequeue را تحلیل زمانی کنید.

class QueueWithTwoStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def insert(self, x):
        self.stack_in.append(x)

    def delete(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            print("Queue is empty")
            return
        return self.stack_out.pop()


# Test
q = QueueWithTwoStacks()
q.insert(10)
q.insert(20)
q.insert(30)
print(q.delete())  # خروجی: 10
print(q.delete())  # خروجی: 20
q.insert(40)
print(q.delete())  # خروجی: 30
print(q.delete())  # خروجی: 40
