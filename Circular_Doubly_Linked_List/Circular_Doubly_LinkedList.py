class DNode:
    def __init__(self,x):
        self.data = x
        self.next = None
        self.back = None

class CDLinkedList:
    def __init__(self):
        self.head = None

    def insert(self,x):
        if self.head is None:
            a = DNode(x)
            self.head = a
            a.next = a
            a.back = a
            return
        a = DNode(x)
        a.back = self.head.back
        a.next = self.head
        self.head.back.next = a
        self.head.back = a

    def insert_after(self,x,y):
        if self.head is None:
            return
        if self.head.next is self.head:  # تک عضوی
            if self.head.data == x:
                a = DNode(y)
                a.back = self.head
                self.head.back = a
                a.next = self.head
                self.head.next = a
                return
        c = self.head
        while c.data != x:
            c = c.next
            if c == self.head:  # یک دور
                return
        a = DNode(y)
        a.next = c.next
        a.back = c
        c.next.back = a
        c.next = a

    def insert_before(self,x,y):
        if self.head is None:
            return
        if self.head.next is self.head:  # تک عضوی
            if self.head.data == x:
                a = DNode(y)
                a.next = self.head
                a.back = self.head
                self.head.next = a
                self.head.back = a
                self.head = a
                return
        c = self.head
        while c.next.data != x:
            c = c.next
            if c.next == self.head:  # یک دور
                return
        a = DNode(y)
        a.next = c.next
        a.back = c
        c.next.back = a
        c.next = a

    def delete(self):
        if self.head is None:
            return
        if self.head.next is self.head:  # تک عضوی
            del self.head
            self.head = None
            return
        c = self.head
        c.back.next = c.next
        c.next.back = c.back
        self.head = c.next
        del c

    def delete_after(self, x):
        if self.head is None:
            return
        if self.head.next is self.head:  # تک عضوی
            if self.head.data == x:
                del self.head
                self.head = None
            return
        c = self.head
        while True:
            if c.data == x:
                c1 = c.next
                if c1 == self.head:
                    self.head = self.head.next
                c.next = c1.next
                c1.next.back = c
                del c1
            c = c.next
            if c == self.head:  # یک دور
                return

    def delete_before(self,x):
        if self.head is None:
            return
        if self.head.next is self.head:  # تک عضوی
            return
        c = self.head
        while True:
            if c.next.data == x:
                c1 = c
                if c1 == self.head:
                    self.head = self.head.next
                c1.back.next = c1.next
                c1.next.back = c1.back
                del c1
            c = c.next
            if c == self.head:  # یک دور
                return

    def delete_x(self,x):
        if self.head is None:
            return
        if self.head.next is self.head:  # تک عضوی
            del self.head
            self.head = None
            return
        c = self.head
        while c.data != x:
            c = c.next
            if c == self.head:  # یک دور
                return
        if c == self.head:
            self.head = self.head.next
        c.back.next = c.next
        c.next.back = c.back
        del c

    def delete_all_x(self,x):
        if self.head is None:
            return
        if self.head.next is self.head:  # تک عضوی
            del self.head
            self.head = None
            return
        c = self.head
        while True:
            if c.data == x:
                c1 = c
                if c1 == self.head:
                    self.head = self.head.next
                c1.back.next = c1.next
                c1.next.back = c1.back
                # c = c.next
                del c1
            c = c.next
            if c == self.head:  # یک دور
                return

    def show(self):
        if self.head is None:
            print("List is empty")
            return
        c = self.head
        while True:
            print(c.data, end=' ↔︎ ')
            c = c.next
            if c == self.head:
                break
        print("(head)")


# Test
ll = CDLinkedList()
ll.insert(44)
ll.insert(0)
ll.insert(45)
ll.insert(7)
ll.insert(0)
ll.insert(19)
ll.insert(5)
ll.insert(9)
ll.insert(2)
ll.insert(0)
ll.insert_after(6,0)
# ll.delete_after(0)
# ll.delete_before(0)
# ll.delete_x(7)
ll.delete_all_x(0)
ll.show()