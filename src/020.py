
x = "Bio"
y = "Informatics"
z = x + y
print(z)


class A:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        return self.val + other.val
    def __mul__(self, other):
        return "__mul__"

a1 = A("a")
a2 = A("b")
print(a1.val + a2.val)
print(a1 + a2)
print(a1 * a2)   # return "__mul__"이 여기로 들어가서 __mul__ 로 나옴


