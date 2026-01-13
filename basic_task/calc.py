class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "not divide by zero"
        return a / b
c = Calculator()

print(c.add(10, 5))
print(c.divide(10, 5))

