def check_h(n):
    while n > 1:
        if n % 2 == 0:
            print(f'Четное {n}')
            n /= 2

        else:
            print(f'Не четное до {n}')
            n = (n*3 + 1)/2
            print(f'Не четное после {n}')


num = int(input())
check_h(num)
print("Конец")