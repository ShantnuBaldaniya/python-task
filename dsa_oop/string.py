class MyString:
    def __init__(self, text):
        self.text = text
    def __add__(self, other):
        return MyString(self.text + other.text)
    def __mul__(self, n):
        return MyString(self.text * n)

a = MyString("Hi")
b = MyString("All")
c = a + b
print(c.text)     
d = a * 2
print(d.text)     
