import inspect


def decorator_(fn):
    c = {}
    def wrapper(*args, **kwargs):
        nonlocal c
        if args[0] not in c:
            c[args[0]] = fn(*args, **kwargs)
            res = fn(*args, **kwargs)
        else: res = 1
        print('c = ', c)
        return res
    return wrapper


@decorator_
def f(n):
    print('func f')
    return n * 123456789

for i in range(5):
    x = int(input('Введите число: '))
    f(x)
