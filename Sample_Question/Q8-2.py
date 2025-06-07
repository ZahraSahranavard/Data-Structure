class BNode:
    def __init__(self,x):
        self.Lchild = None
        self.data = x
        self.Rchild = None

class BTree:
    def __init__(self):
        self.root = None

    def find_LCA_general(self,root, n1, n2):
        if not root:
            return None
        if root.data == n1 or root.data == n2:
            return root
        left = self.find_LCA_general(root.Lchild, n1, n2)
        right = self.find_LCA_general(root.Rchild, n1, n2)

        if left and right:
            return root
        return left if left else right

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
tree = BTree()
tree.insert_left(1)
tree.insert_left(2)
tree.insert_right(3)
tree.insert_left(4)
tree.insert_right(5)
n1, n2 = 4, 5
lca = tree.find_LCA_general(tree.root, n1, n2)
print(f"LCA of {n1} and {n2} is: {lca.data if lca else None}")