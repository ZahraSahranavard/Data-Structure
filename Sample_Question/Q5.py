#     الگوریتمی بنویسید که تشخیص دهد آیا یک لیست پیوندی تکراروندی (Singly Linked List) دارای حلقه است یا خیر. آیا میتوان این کار را با فضای اضافه ی O(1) انجام داد؟

class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def has_cycle(self,head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def insert_last(self, t):
        if self.head is None:
            a = Node(t)
            self.head = a
            return
        a = Node(t)
        c = self.head
        while c.next is not None:
            c = c.next
        c.next = a

    # ایجاد حلقه در لیست: اتصال انتهای لیست به گره با مقدار مشخص
    def create_loop(self, target_data):
        if not self.head:
            return
        loop_target = None
        c = self.head
        while c.next:
            if c.data == target_data:
                loop_target = c
            c = c.next
        if loop_target:
            c.next = loop_target

print("\n---- با حلقه ----")
ll2 = LinkedList()
ll2.insert_last(10)
ll2.insert_last(20)
ll2.insert_last(30)
ll2.insert_last(40)
ll2.insert_last(50)
ll2.create_loop(30)  # ایجاد حلقه: 50 → 30
print("حلقه دارد؟", ll2.has_cycle(ll2.head))