class DNode:
    def __init__(self,x):
        self.data = x
        self.next = None
        self.back = None

class SDLinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self,x):
        if self.head is None:
            a = DNode(x)
            self.head = a
            return
        a = DNode(x)
        a.next = self.head
        self.head.back = a
        self.head = a

    def insert_last(self,x):
        if self.head is None:
            a = DNode(x)
            self.head = a
            return
        a = DNode(x)
        c = self.head
        while c.next:
            c = c.next
        c.next = a
        a.back = c

    def insert_after(self,x,y):
        if self.head is None:
            return
        if self.head.next is None:  # تک عضوی
            if self.head.data == x:
                self.insert_last(y)
                return
        c = self.head
        while c.data != x:
            c = c.next
            if c is None:  # عدم وجود
                return
        a = DNode(y)
        a.next = c.next
        c.next = a
        a.next.back = a
        a.back = c

    def insert_before(self,x,y):
        if self.head is None:
            return
        if self.head.next is None:  # تک عضوی
            if self.head.data == x:
                self.insert_first(y)
                return
        c = self.head
        while c.next.data != x:
            c = c.next
            if c.next is None:  # عدم وجود
                return
        a = DNode(y)
        a.next = c.next
        c.next.back = a
        c.next = a
        a.back = c

    def delete_first(self):
        if self.head is None:
            return
        if self.head.next is None:  # تک عضوی
            del self.head
            self.head = None
        c = self.head
        self.head = self.head.next
        del c
        self.head.back = None

    def delete_last(self):
        if self.head is None:
            return
        if self.head.next is None:  # تک عضوی
            del self.head
            self.head = None
        c = self.head
        while c.next is not None:
            c = c.next
        c.back.next = None
        del c

    def delete_after(self,x):
        if self.head is None:
            return
        if self.head.next is None:  # تک عضوی
            return
        c = self.head
        while c.data != x:
            c = c.next
            if c is None:  # عدم وجود
                return
        c1 = c.next
        if c1.next == None:
            self.delete_last()
            return
        c.next = c1.next
        c1.next.back = c
        del c1

    def delete_before(self,x):
        if self.head is None:
            return
        if self.head.next is None:
            return
        c = self.head
        while c.next.data != x:
            c = c.next
            if c.next is None:  # عدم وجود
                return
        if self.head.next.data == x:
            self.delete_first()
            return
        c.back.next = c.next
        c.next.back = c.back
        del c

    def delete_x(self,x):
        if self.head is None:
            return
        c = self.head  # عدم وجود x
        while c.data != x:
            c = c.next
            if c is None:
                return
        if c.next is None:  # گره آخر
            self.delete_last()
            return
        if c.back is None:  # گره اول
            self.delete_first()
            return
        c.back.next = c.next
        c.next.back = c.back
        del c

    def show(self):
        c = self.head
        while c is not None:
            print(c.data, end=' ↔︎ ')
            c = c.next
        print('None')  # برای رفتن به خط بعد بعد از پایان چاپ



# Test
ll = SDLinkedList()
ll.insert_first(5)
ll.insert_first(9)
ll.insert_first(8)
ll.insert_first(10)
ll.insert_first(2)
ll.insert_before(5, 20)
ll.insert_after(8,30)
ll.delete_x(5)
ll.delete_last()
ll.delete_first()
ll.delete_after(30)
ll.insert_first(0)
ll.insert_first(42)
ll.insert_first(1)
ll.delete_before(42)
ll.show()
