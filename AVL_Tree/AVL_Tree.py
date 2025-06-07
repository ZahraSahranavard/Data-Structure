class AVLNode:
    def __init__(self, data):
        self.data = data
        self.Lchild = None
        self.Rchild = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

# ------------------------------------------- Methods -----------------------------------------------

    def get_height(self, node):
        if not node:
            return 0
        return node.height


    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.Lchild) - self.get_height(node.Rchild)


    def right_rotate(self, y): # balance > 1
        x = y.Lchild
        T2 = x.Rchild
        x.Rchild = y
        y.Lchild = T2
        y.height = 1 + max(self.get_height(y.Lchild), self.get_height(y.Rchild))
        x.height = 1 + max(self.get_height(x.Lchild), self.get_height(x.Rchild))
        return x


    def left_rotate(self, x):  # balance < -1
        y = x.Rchild
        T2 = y.Lchild
        y.Lchild = x
        x.Rchild = T2
        x.height = 1 + max(self.get_height(x.Lchild), self.get_height(x.Rchild))
        y.height = 1 + max(self.get_height(y.Lchild), self.get_height(y.Rchild))
        return y


    def left_right_rotate(self, z):  # balance > 1
        z.Lchild = self.left_rotate(z.Lchild)
        return self.right_rotate(z)


    def right_left_rotate(self, z):  # balance < -1
        z.Rchild = self.right_rotate(z.Rchild)
        return self.left_rotate(z)


    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.data:
            root.Lchild = self.insert(root.Lchild, key)
        else:
            root.Rchild = self.insert(root.Rchild, key)

        root.height = 1 + max(self.get_height(root.Lchild), self.get_height(root.Rchild))
        balance = self.get_balance(root)

        # right rotate (LL)
        if balance > 1 and key < root.Lchild.data:
            return self.right_rotate(root)

        # left rotate (RR)
        if balance < -1 and key > root.Rchild.data:
            return self.left_rotate(root)

        # left_right rotate (LR)
        if balance > 1 and key > root.Lchild.data:
            return self.left_right_rotate(root)

        # right_left rotate (RL)
        if balance < -1 and key < root.Rchild.data:
            return self.right_left_rotate(root)
        return root
    def add(self, key):
        self.root = self.insert(self.root, key)


    #  حذف چپ ترین نود (کوچک ترین)
    def delete_min(self):
        self.root = self.delete_min_recursive(self.root)
    def delete_min_recursive(self, node):
        if node.Lchild is None:
            return node.Rchild
        node.Lchild = self.delete_min_recursive(node.Lchild)
        node.height = 1 + max(self.get_height(node.Lchild), self.get_height(node.Rchild))
        balance = self.get_balance(node)
        if balance > 1:
            if self.get_balance(node.Lchild) >= 0:
                return self.right_rotate(node)
            else:
                node.Lchild = self.left_rotate(node.Lchild)
                return self.right_rotate(node)

        if balance < -1:
            if self.get_balance(node.Rchild) <= 0:
                return self.left_rotate(node)
            else:
                node.Rchild = self.right_rotate(node.Rchild)
                return self.left_rotate(node)
        return node


    #  حذف راست ترین نود (بزرگ ترین)
    def delete_max(self):
        self.root = self.delete_max_node(self.root)
    def delete_max_node(self, node):
        if node.Rchild is None:
            return node.Lchild
        node.Rchild = self.delete_max_node(node.Rchild)
        node.height = 1 + max(self.get_height(node.Lchild), self.get_height(node.Rchild))
        balance = self.get_balance(node)

        if balance > 1:
            if self.get_balance(node.Lchild) >= 0:
                return self.right_rotate(node)  # LL case
            else:
                node.Lchild = self.left_rotate(node.Lchild)  # LR case
                return self.right_rotate(node)

        if balance < -1:
            if self.get_balance(node.Rchild) <= 0:
                return self.left_rotate(node)  # RR case
            else:
                node.Rchild = self.right_rotate(node.Rchild)  # RL case
                return self.left_rotate(node)
        return node

    def delete_x(self,root,key):
        if not root:
            return root
        if key < root.data:
            root.Lchild = self.delete_x(root.Lchild, key)
        elif key > root.data:
            root.Rchild = self.delete_x(root.Rchild, key)
        else:
            # حالت ۱: بدون فرزند یا فقط یکی
            if not root.Lchild:
                return root.Rchild
            elif not root.Rchild:
                return root.Lchild

            # حالت ۲: دو فرزند - جانشین را پیدا کن
            temp = self.get_min_value_node(root.Rchild)
            root.data = temp.data
            root.Rchild = self.delete_x(root.Rchild, temp.data)
        root.height = 1 + max(self.get_height(root.Lchild), self.get_height(root.Rchild))
        balance = self.get_balance(root)

        # Left Left
        if balance > 1 and self.get_balance(root.Lchild) >= 0:
            return self.right_rotate(root)

        # Left Right
        if balance > 1 and self.get_balance(root.Lchild) < 0:
            root.Lchild = self.left_rotate(root.Lchild)
            return self.right_rotate(root)

        # Right Right
        if balance < -1 and self.get_balance(root.Rchild) <= 0:
            return self.left_rotate(root)

        # Right Left
        if balance < -1 and self.get_balance(root.Rchild) > 0:
            root.Rchild = self.right_rotate(root.Rchild)
            return self.left_rotate(root)
        return root
    def get_min_value_node(self, node):
        current = node
        while current.Lchild:
            current = current.Lchild
        return current


    def search(self, x):
        found = self.search_recursive(self.root, x)
        if found:
            print(f"{x} Found.")
        else:
            print(f"{x} Not Found.")
        return
    def search_recursive(self, root, x):
        if root is None:
            return
        if root.data == x:
            return root
        else:
            if x > root.data:
                return self.search_recursive(root.Rchild, x)
            return self.search_recursive(root.Lchild, x)

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

    #  متن replce طبق قوانین درخت AVL:
    def safe_replace(self,x,y):
        if self.search_recursive(self.root, x) is None:
            print(f"{x} Not Found.")
            return
        self.delete_x(self.root,x)
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

# ----------------------------------------------------------------------------------------------------

# Test
avl = AVLTree()
avl.root = AVLNode(50)
avl.add(70)
avl.add(15)
avl.add(23)
avl.add(65)
avl.add(68)
avl.search(50)
avl.delete_x(avl.root,70)


# avl.display_NLR()
# avl.display_LRN()
avl.display_LNR()
