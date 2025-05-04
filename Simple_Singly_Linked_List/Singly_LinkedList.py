class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self,t):
        if self.head is None:
            a = Node(t)
            a.next = self.head
            self.head = a
            return
        a = Node(t)
        a.next = self.head
        self.head = a

    def insert_last(self,t):
        if self.head is None:
            a = Node(t)
            self.head = a
            return
        a = Node(t)
        c = self.head
        while c.next is not None:
            c = c.next
        c.next = a

    def insert_after(self,x,t):
        if self.head is None:
            return
        c = self.head
        while c.data != x:
            if c.next is None:
                return
            c = c.next
        a = Node(t)
        a.next = c.next
        c.next = a

    def insert_before(self,x,t):
        if self.head is None:
            return
        if self.head.next is None:  # تک گره
            if self.head.data == x:
                self.insert_first(t)
                return
        c = self.head
        while c is not None:
            if c.next.data == x:
                a = Node(t)
                a.next = c.next
                c.next = a
                return
            c = c.next
        print("Error")

    def delete_first(self):
        if self.head is None:
            return
        c = self.head
        self.head = self.head.next
        del c

    def delete_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            del self.head
            self.head = None
            return
        c = self.head
        while c.next.next:
            c = c.next
        del c.next
        c.next = None

    def delete_after(self,x):
        if self.head is None:
            return
        if self.head.next is None:
            return
        c = self.head
        while c:
            if c.data == x:
                if c.next == None:
                    return
                a = c.next
                c.next = c.next.next
                del a
                return
            c = c.next

    def delete_before(self,x):
        if self.head is None:
            return
        if self.head.next is None:  # تک گره
            return
        if self.head.next.data == x:  # دو گره
            c = self.head
            self.head = self.head.next
            del c
            return
        c = self.head
        while c.next.next is not None:
            if c.next.next.data == x:
                a = c.next
                c.next = c.next.next
                del a
                return
            c = c.next

    def show(self):
        c = self.head
        while c:
            print(c.data, end=' -> ')
            c = c.next
        print('None')


# Test
ll = LinkedList()
ll.insert_first(5)
ll.insert_first(9)
ll.insert_last(64)
ll.insert_last(12)
ll.insert_first(10)
ll.insert_first(2)
ll.insert_before(5,555)
ll.insert_after(64,11)
ll.delete_last()
ll.delete_first()
ll.delete_after(9)
ll.delete_before(64)
ll.show()