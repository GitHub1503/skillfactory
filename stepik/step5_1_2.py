a,b,c,d = int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: '))
t1, t2 = 0, 0
if (a%2 == 0 and b%2 == 0) or (a%2 != 0 and b%2 != 0):
    t1 = 1
elif (a%2 == 0 and b%2 != 0) or (a%2 != 0 and b%2 == 0):
    t1 = 2
if (c%2 == 0 and d%2 == 0) or (c%2 != 0 and d%2 != 0):
    t2 = 1
elif (c%2 == 0 and d%2 != 0) or (c%2 != 0 and d%2 == 0):
    t2 = 2

if t1 == t2:
    print('YES')
else:
    print('NO')