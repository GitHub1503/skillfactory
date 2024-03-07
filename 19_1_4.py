def stars_triangle(n):
    for i in range(n):
        print('*' * (i+n))
        n -= 2

stars_triangle(7)