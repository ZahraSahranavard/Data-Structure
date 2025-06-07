
#     تابعی بنویسید که دو گره در یک درخت جستجوی دودویی (BST) دریافت کند و کوچکترین جد مشترک آنها را برگرداند. آیا این کار برای درخت دودویی معمولی (نه BST) هم قابل انجام است؟

class BNode:
    def __init__(self,x):
        self.Lchild = None
        self.data = x
        self.Rchild = None

class Binary_Search_Tree:
    def __init__(self):
        self.root = None
        self.l = []

    def find_LCA_BST(self,root, n1, n2):
        if not root:
            return None
        if n1 < root.data and n2 < root.data:
            return self.find_LCA_BST(root.Lchild, n1, n2)
        if n1 > root.data and n2 > root.data:
            return self.find_LCA_BST(root.Rchild, n1, n2)
        return root

    def add(self,x):
        if self.root is None:
            self.root = BNode(x)
            self.l.append(x)
            return
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

# Test
bst = Binary_Search_Tree()
for val in [20, 10, 30, 5, 15, 25, 40]:
    bst.add(val)

lca = bst.find_LCA_BST(bst.root, 5, 15)
print("LCA:", lca.data)  # خروجی: 10

lca = bst.find_LCA_BST(bst.root, 5, 30)
print("LCA:", lca.data)  # خروجی: 20
