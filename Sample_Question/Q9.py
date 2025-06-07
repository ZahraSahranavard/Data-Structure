
#    الگوریتمی بنویسید که پیمایش Inorder یک درخت دودویی را بدون بازگشت و با استفاده از یک پشته انجام دهد. تحلیل زمانی آن چیست؟

class BNode:
    def __init__(self,x):
        self.Lchild = None
        self.data = x
        self.Rchild = None

class BTree:
    def __init__(self):
        self.root = None

    def inorder_iterative(self,root):  #  Left - Node - Right
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.Lchild
            current = stack.pop()
            print(current.data, end=' ')
            current = current.Rchild

    def insert_left(self,d):
        if self.root is None:  # اگر رشه خالی بود:
            self.root = BNode(d)
            return
        c = self.root
        while c.Lchild is not None:
            c = c.Lchild
        c.Lchild = BNode(d)

    def insert_right(self,d):
        if self.root is None:
            self.root = BNode(d)
            return
        c = self.root
        while c.Rchild is not None:
            c = c.Rchild
        c.Rchild = BNode(d)

# Test
bt = BTree()
bt.root = BNode(70)
bt.insert_left(2)
bt.insert_left(6)
bt.insert_left(12)
bt.insert_right(30)
bt.insert_right(8)
bt.inorder_iterative(bt.root)

# تحلیل زمانی:
# تمام گره‌ها دقیقاً یک‌بار وارد پشته و یک‌بار از آن خارج می‌شوند →
# ⏱ O(n) برای n گره.