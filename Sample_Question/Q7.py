
#  الگوریتمی بنویسید که یک درخت دودویی را بهصورت مورب پیمایش کند و مقادیر هر مورب را چاپ کند.
#    مثال:
#        1
#        \/
#      2   3
#      \/  \/
#    4  5 6  7
#    خروجی: [1, 3, 7], [2, 5, 6], [4]

from collections import defaultdict

class BNode:
    def __init__(self, x):
        self.data = x
        self.Lchild = None
        self.Rchild = None

def diagonal_traversal(root):
    result = defaultdict(list)

    def helper(node, diagonal):
        if not node:
            return
        # گره را به لیست مورب فعلی اضافه کن
        result[diagonal].append(node.data)
        # به سمت چپ برو، مورب را افزایش بده
        helper(node.Lchild, diagonal + 1)
        # به سمت راست برو، مورب ثابت بماند
        helper(node.Rchild, diagonal)

    helper(root, 0)
    # مرتب‌سازی نتایج بر اساس شماره مورب و تبدیل به لیست خروجی
    return [result[d] for d in sorted(result)]

# نمونه تست:
root = BNode(1)
root.Lchild = BNode(2)
root.Rchild = BNode(3)
root.Lchild.Lchild = BNode(4)
root.Lchild.Rchild = BNode(5)
root.Rchild.Lchild = BNode(6)
root.Rchild.Rchild = BNode(7)

output = diagonal_traversal(root)
print(output)  # خروجی: [[1, 3, 7], [2, 5, 6], [4]]
