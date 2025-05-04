# متدی به کلاس لیست پیوندی یک طرفه ساده اضافه کنید که گره ای را به وسط لیست اضافه کند.

class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_last(self,t):
        if self.head is None:
            n = Node(t)
            self.head = n
            return
        n = Node(t)
        c = self.head
        while c.next is not None:
            c = c.next
        c.next = n

    def insert_mid(self, t):  # Answer the question
        if self.head is None:
            return
        if self.head.next is None:
            a = Node(t)
            a.next = self.head
            self.head = a
            return
        c = self.head
        count = 0
        while c is not None:
            count += 1
            c = c.next
        mid = count // 2
        c = self.head
        for i in range(mid):
            c = c.next
        a = Node(t)
        a.next = c.next
        c.next = a
        text = f"Inserted {t} at position {mid + 1}"
        print(text)

    def show(self):
        c = self.head
        while c:
            print(c.data, end=' -> ')
            c = c.next
        print('None')

# Test
ll = LinkedList()
ll.insert_last(17)
ll.insert_last(8)
ll.insert_last(10)
ll.insert_last(3)
ll.insert_last(23)
ll.insert_mid(5)
ll.show()