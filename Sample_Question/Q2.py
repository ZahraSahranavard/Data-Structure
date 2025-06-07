
#     تابعی بنویسید که یک رشته شامل پرانتزهای (), [], {} را بررسی کند و تشخیص دهد آیا پرانتزها به درستی بسته شدهاند یا خیر.
#    مثال صحیح: "{[()]}"
#    مثال نادرست: "[(])"

def is_balanced(s):
    stack = []
    opening = "([{"
    closing = ")]}"
    matches = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != matches[char]:
                return False
            stack.pop()

    return len(stack) == 0

print(is_balanced("{[()]}"))  # خروجی: True
print(is_balanced("[(])"))    # خروجی: False
print(is_balanced("(()[]{})")) # خروجی: True
print(is_balanced("((())"))    # خروجی: False
