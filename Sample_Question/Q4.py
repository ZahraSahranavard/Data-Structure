

#     یک صف اولویت دار (Priority Queue) با استفاده از لیست پیوندی پیاده سازی کنید. در این صف، عناصر با اولویت بالاتر زودتر حذف میشوند.

class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority    # عدد اولویت (کمتر = مهم‌تر)
        self.next = None
class PriorityQueue:
    def __init__(self):
        self.head = None

    def insert(self, data, priority):
        a = Node(data, priority)
        if self.head is None or priority < self.head.priority:
            a.next = self.head
            self.head = a
        else:
            c = self.head
            while c.next and c.next.priority <= priority:
                c = c.next
            a.next = c.next
            c.next = a

    def delete(self):
        if self.head is None:
            print("Queue is empty")
            return
        data = self.head.data
        self.head = self.head.next
        return data

    def show(self):
        c = self.head
        while c:
            print(f"({c.data}, priority={c.priority})", end=" -> ")
            c = c.next
        print("None")


# Test
pq = PriorityQueue()
pq.insert("Task A", 3)
pq.insert("Task B", 1)
pq.insert("Task C", 2)
pq.insert("Task D", 4)
pq.show()
print("Dequeue:", pq.delete())



