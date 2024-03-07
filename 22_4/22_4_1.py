def p(n):
    if n>0:
        p(n-1)
        print(n)
    else:
        return

p(7)