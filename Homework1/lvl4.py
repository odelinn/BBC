import math

class Calculator:
    def base_oper(self, a, sign, b):
        if sign == "+": return a + b
        if sign == "-": return a - b
        if sign == "*": return a * b
        if sign == "/": return a / b
    def triga(self, func, x):
        if func == "sin": return math.sin(x)
        if func == "cos": return math.cos(x)
        if func == "tg": return math.tan(x)

c = Calculator()
method = input()

if method == "base_oper":
    a = float(input())
    b = float(input())
    sign = input()
    print(c.base_oper(a, sign, b))
elif method == "triga":
    func = input()
    x = float(input())
    print(c.triga(func, x))
