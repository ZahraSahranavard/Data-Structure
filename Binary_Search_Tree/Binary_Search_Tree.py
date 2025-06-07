class BNode:
    def __init__(self,x):
        self.Lchild = None
        self.data = x
        self.Rchild = None

class Binary_Search_Tree:
    def __init__(self):
        self.root = None
        self.l = []
# ------------------------------------------- Methods -----------------------------------------------
    #  اضافه کردن عنصر جدید در محل مناسب
    def add(self,x):
        if self.root is None:
            self.root = BNode(x)
            self.l.append(x)
        self.padd(self.root,x)
    def padd(self,root,x):
        if x > root.data:
            if root.Rchild == None:
                root.Rchild = BNode(x)
                self.l.append(x)
            self.padd(root.Rchild,x)  # پیمایش سمت راست
        if x < root.data:
            if root.Lchild is None:
                root.Lchild = BNode(x)
                self.l.append(x)
            self.padd(root.Lchild,x)
        return

    #  حذف چپ ترین نود (کوچک ترین)
    def delete_min(self):
        if self.root is None:
            return
        if self.root.Lchild is None:  # کوچک‌ترین مقدار خود ریشه است
            self.root = self.root.Rchild
            return
        c = self.root
        c1 = self.root.Lchild
        while c1.Lchild:
            c = c1
            c1 = c1.Lchild
        c.Lchild = c1.Rchild
        del c1


    #  حذف راست ترین نود (بزرگ ترین)
    def delete_max(self):
        if self.root is None:
            return
        if self.root.Rchild is None:
            self.root = self.root.Lchild
            return
        c = self.root
        c1 = self.root.Rchild
        while c1.Rchild:
            c = c1
            c1 = c1.Rchild

        c.Rchild = c1.Lchild
        del c1


    #   حذف عنصر x از درخت
    def delete_x(self, x):
        if self.root is None:
            return
        parent = None
        current = self.root
        while current:
            if x < current.data:
                parent = current
                current = current.Lchild
            elif x > current.data:
                parent = current
                current = current.Rchild
            else:
                break  # گره پیدا شد
        if current is None:  #  گره وجود ندارد
            print("Node not found.")
            return

        # حالت 1: گره بدون فرزند (برگ)
        if current.Lchild is None and current.Rchild is None:
            if parent:  # گره والد دارد
                if parent.Lchild == current:
                    parent.Lchild = None
                else:
                    parent.Rchild = None
            else:  # تک عضوی: فقط ریشه
                self.root = None

        # حالت 2: فقط یک فرزند دارد
        elif (current.Lchild is None and current.Rchild is not None) or (current.Lchild is not None and current.Rchild is None):
            child = current.Lchild if current.Lchild else current.Rchild
            if parent:
                if parent.Lchild == current:
                    parent.Lchild = child
                else:
                    parent.Rchild = child
            else:
                self.root = child

        # حالت 3: دو فرزند دارد
        else:
            # پیدا کردن کوچک‌ترین مقدار در زیر درخت راست
            successor_parent = current  # والد جانشین
            successor = current.Rchild  # زیر درخت سمت راست گره current
            while successor.Lchild:
                successor_parent = successor
                successor = successor.Lchild
            current.data = successor.data  # جایگزینی داده
            # حذف successor
            if successor_parent.Lchild == successor:
                successor_parent.Lchild = successor.Rchild
            else:
                successor_parent.Rchild = successor.Rchild


    def search(self,x):
        found = self.search_recursive(self.root,x)
        if found:
            print(f"{x} Found.")
        else:
            print(f"{x} Not Found.")
        return
    def search_recursive(self,root,x):
        if root is None:
            return
        if root.data == x:
            return root
        else:
            if x > root.data:
                return self.search_recursive(root.Rchild,x)
            return self.search_recursive(root.Lchild,x)


    def replace(self,x,y):
        self.replace_recursive(self.root,x,y)
    def replace_recursive(self,node,x,y):
        if node is None:
            return
        if node.data == x:
            node.data = y
        elif x < node.data:
            self.replace_recursive(node.Lchild,x,y)
        else:
            self.replace_recursive(node.Rchild,x,y)


    #  متن replce طبق قوانین درخت BST:
    def safe_replace(self,x,y):
        if self.search_recursive(self.root, x) is None:
            print(f"{x} Not Found.")
            return
        self.delete_x(x)
        self.add(y)
        print(f"{x} replaced with {y}.")

    # ------------------------------------------- Traversals -----------------------------------------------

    #  پیمایش پیش ترتیب (Preorder Traversal)
    def display_NLR(self):  # Node - Left - Right
        print("\nPreorder Traversal:")
        self.show_NLR(self.root)
    def show_NLR(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.show_NLR(root.Lchild)
            self.show_NLR(root.Rchild)


    #  پیمایش میان ترتیب (Inorder Traversal)
    def display_LNR(self):  # Left - Node - Right
        print("\nInorder Traversal:")
        self.show_LNR(self.root)
    def show_LNR(self, root):
        if root is not None:
            self.show_LNR(root.Lchild)
            print(root.data, end=" ")
            self.show_LNR(root.Rchild)


    #  پیمایش میان ترتیب (Postorder Traversal)
    def display_LRN(self):  # Left - Right - Node
        print("\nPostorder Traversal:")
        self.show_LRN(self.root)
    def show_LRN(self, root):
        if root is not None:
            self.show_LRN(root.Lchild)
            self.show_LRN(root.Rchild)
            print(root.data, end=" ")


    # Level order
    def show_BFS(self):
        if not self.root:
            return
        q = [self.root]
        print("\nLevel order:")
        while q:
            node = q.pop(0)
            print(node.data, end=" ")
            if node.Lchild:
                q.append(node.Lchild)
            if node.Rchild:
                q.append(node.Rchild)
# ---------------------------------------------- Practice --------------------------------------------------

# سوال1: تابعی بنویسید که یک BST را از ورودی گرفته و لیست مربوط به آن را بازگرداند.
def create_list(tree):
    print(tree.l)

#  سوال2: تابعی بنویسید که یک لیست از ورودی گرفته و BST مربوط به آن را برگرداند.
def create_tree(a):
    tree = Binary_Search_Tree()
    for i in a:
        tree.add(i)
    return tree

# ----------------------------------------------------------------------------------------------------

# Test
bst = Binary_Search_Tree()
bst.root = BNode(70)
bst.add(100)
bst.add(60)
bst.add(250)
bst.add(35)
bst.add(15)
bst.search(34)
bst.add(300)
# bst.replace(250,2)
bst.delete_x(15)
# bst.replace_new(60,140)


# data = [45,70,103,240,12,56,400]
# tree = create_tree(data)
# tree.display_NLR()

# create_list(bst)


# bst.display_NLR()
# bst.display_LRN()
bst.display_LNR()
