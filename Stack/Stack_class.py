class Stack:
    
    def __init__(self, l=100):
        self.list = []
        self.top = -1
        self.limit = l
        
    def push(self,x):
        if len(self.list) >= self.limit:
            return ('stack is full')
        self.list.append(x)
        self.top += 1

    def pop(self):
        if self.top == -1:
            print('stack is empty')
            return
        self.top -= 1
        return self.list.pop()

    def peek(self):
        if self.top == -1:
            print('stack is empty')
            return
        return self.list[-1]

    def is_find (self,x):
        for i in range(self.top + 1):
            if self.list[i] == x:
                return True
        return False

    def is_full(self):
        return self.top == self.limit - 1

    def is_empty(self):
        return self.top == -1

    def is_mid(self):
        return self.top == (self.limit // 2) - 1

    def replace(self, old_value, new_value):
        temp_list = []
        while not self.is_empty():
            item = self.pop()
            if item == old_value:
                temp_list.append(new_value)
            else:
                temp_list.append(item)
        while temp_list:
            self.push(temp_list.pop())
            
    def show(self):
        if self.top == -1:
            print('stack is empty')
            return
        print("Stack (Top to Bottom):")
        for i in range(self.top,-1,-1):
            print(self.list[i])


limit = int(input("Enter stack limit: "))
s1 = Stack(limit)

for i in range(limit):
    value = input("Enter value to push: ")
    s1.push(value)
    
s1.show()
