def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

result = add(234,234, 2, 54,2, 45, 5)
print(result)

def calculate(**kwargs):
    print(kwargs)

calculate(add=34, mult=34, plus=234)