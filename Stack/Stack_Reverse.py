# تابعی بنویسید که با پیروی از قانون پشته، داده های درون استک را برعکس کند.

from Stack_class import Stack

def Rev(s1):
    s2 = Stack(10)
    s3 = Stack(10)

    for i in range(s1.top + 1):
        s2.push(s1.pop())

    for i in range(s2.top + 1):
        s3.push(s2.pop())

    for i in range(s3.top + 1):
        s1.push(s3.pop())
