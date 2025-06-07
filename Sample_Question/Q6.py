
#    تابعی بنویسید که یک لیست پیوندی را به صورت گروهی (هر k گره) معکوس کند.
#    مثال:
#    ورودی: 1→2→3→4→5, k = 2
#    خروجی: 2→1→4→3→5

class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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

    def reverse_k_group(self, head, k):
        current = head
        prev = None
        count = 0
        temp = head
        for i in range(k):
            if not temp:
                return head
            temp = temp.next
        while current and count < k:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            count += 1
        if current:  # سر گروه بعدی
            head.next = self.reverse_k_group(current, k)
        return prev
    def show(self):
        c = self.head
        while c:
            print(c.data, end=' -> ')
            c = c.next
        print('None')

ll = LinkedList()
for i in range(1, 6):
    ll.insert_last(i)
print("Before reversing:")
ll.show()
k = 2
ll.head = ll.reverse_k_group(ll.head, k)
print("After reversing:")
ll.show()
