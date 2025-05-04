class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class CSLinkedList:
    def __init__(self):
        self.head = None

    def insert(self,x):
        if self.head is None:
            a = Node(x)
            self.head = a
            self.head.next = a
            return
        a = Node(x)
        a.next = self.head
        c = self.head
        while c.next != self.head:
            c = c.next
        c.next = a
        self.head = a

    def insert_after(self,x,t):
        if self.head is None:
            return
        if self.head.next == self.head:  # تک گره
            if self.head.data == x:
                a = Node(t)
                a.next = self.head
                self.head.next = a
            return
        c = self.head  # معمولی
        while True:
            if c.data == x:
                a = Node(t)
                a.next = c.next
                c.next = a
                return
            c = c.next

    def insert_before(self,x,t):
        if self.head is None:
            return
        if self.head.next == self.head:  # تک گره
            if self.head.data == x:
                a = Node(t)
                a.next = self.head
                self.head = a
                self.head.next.next = self.head
            return
        if self.head.data == x:  # گره اول
            a = Node(t)
            c = self.head
            while c.next != self.head:
                c = c.next
            c.next = a
            a.next = self.head
            self.head = a
            return
        c = self.head  # معمولی
        while c.next != self.head:
            if c.next.data == x:
                a = Node(t)
                a.next = c.next
                c.next = a
                return
            c = c.next

    def delete(self):
        if self.head is None:
            return
        if self.head.next is None:  # تک گره
            del self.head
            self.head = None
            return
        c = self.head
        while c.next != self.head:
            c = c.next
        c.next = self.head.next
        del self.head
        self.head = c.next

    def delete_after(self,x):
        if self.head is None:
            return
        if self.head.next == self.head:  # تک گره
            if self.head.data == x:
                del self.head
                self.head = None
            return
        c = self.head
        while c.data != x:
            c = c.next
            if c == self.head:  # یک دور
                return
        c1 = c.next
        c.next = c1.next
        if c1 == self.head:
            self.head = c1.next
        del c1

    def delete_before(self,x):
        if self.head is None:
            return
        if self.head.next == self.head:  # تک گره
            if self.head.data == x:
                del self.head
                self.head = None
            return
        if self.head.data == x:  # گره اول
            c = self.head
            while c.next.next != self.head:
                c = c.next
            c1 = c.next
            c.next = self.head
            del c1
            return
        c = self.head
        while c.next.next.data != x:
            c = c.next
            if c.next.next == self.head:  # یک دور
                return
        c1 = c.next
        c.next = c1.next
        del c1

    def show(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")


ll = CSLinkedList()
ll.insert(5)
ll.insert(7)
ll.insert(0)
ll.insert(62)
ll.insert(23)
ll.insert(4)
ll.insert_before(4,9)
ll.delete_before(4)
ll.insert_after(5,6)
ll.delete_after(6)
ll.show()