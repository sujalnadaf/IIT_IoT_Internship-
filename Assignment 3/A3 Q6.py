def add(a, b): return a + b
def sub(a, b): return a - b
def calculate(a, b, func):
    return func(a, b)
print(calculate(5, 3, add))
print(calculate(5, 3, sub))