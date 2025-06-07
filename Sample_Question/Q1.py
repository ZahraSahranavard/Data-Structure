
#  الگوریتمی بنویسید که یک عبارت ریاضی در نمادگذاری پسوندی (مثل 3 4 + 5 *) را دریافت کرده و مقدار آن را محاسبه کند. از یک پشته برای حل مسئله استفاده کنید.

def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for i in tokens:
        if i.isdigit():  # اگر عدد باشد
            stack.append(int(i))
        else:  # اگر عملگر باشد
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(a - b)
            elif i == '*':
                stack.append(a * b)
            elif i == '/':
                stack.append(a / b)  # تقسیم اعشاری
            else:
                raise ValueError(f"Invalid operator: {i}")

    return stack.pop()

expr = "3 4 + 5 *"
result = evaluate_postfix(expr)
print(result)  # خروجی: 35
