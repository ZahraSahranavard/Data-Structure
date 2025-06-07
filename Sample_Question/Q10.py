
#     چگونه میتوان یک سیستم کش LRU (Least Recently Used) را با ترکیب یک صف (بر اساس لیست پیوندی) و یک هش مپ پیادهسازی کرد؟ عملیات get و put را شرح دهید.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> node
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _insert_at_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    # O(1)      مقدار رو برمی‌گردونه و گره رو میاره جلو (یعنی اخیراً استفاده‌شده).
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert_at_front(node)
            return node.value
        return -1

    # مقدار جدید می‌ذاره، و اگر کش پر بود، قدیمی‌ترین مقدار رو حذف می‌کنه.     O(1)
    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._insert_at_front(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

    def show(self):
        current = self.head.next
        print("Cache state (newest → oldest):")
        while current != self.tail:
            print(f"Key: {current.key}, Value: {current.value}")
            current = current.next
        print("-" * 30)


# Test
# ایجاد کش با ظرفیت 2
cache = LRUCache(2)
cache.put(1, 100)   # کش: {1=100}
cache.put(2, 200)   # کش: {2=200, 1=100}

print(cache.get(1))  # خروجی: 100 → حالا 1 میشه جدیدترین استفاده‌شده، کش: {1=100, 2=200}

# افزودن مقدار جدید (کش پره، باید 2 حذف شه چون کم‌استفاده‌ترینه)
cache.put(3, 300)   # کش: {3=300, 1=100}

print(cache.get(2))  # خروجی: -1 (چون 2 حذف شده)
print(cache.get(3))  # خروجی: 300
print(cache.get(1))  # خروجی: 100

# افزودن مقدار جدید، باید 3 حذف شه چون الان کم‌استفاده‌ترینه
cache.put(4, 400)   # کش: {4=400, 1=100}

print(cache.get(3))  # خروجی: -1
print(cache.get(4))  # خروجی: 400
print(cache.get(1))  # خروجی: 100
cache.show()