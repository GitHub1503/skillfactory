tickets = int(input('Введите колличество билетов: '))
cost1, cost2, cost3 = 0, 990, 1390  # Стимость билетов в зависимости от возроста
price = 0   # Общая стимость всех билетоа
age = [input('Введите возраст посетителей: ') for i in range(tickets)]

for i in range(len(age)):
    if int(age[i]) < 18:
        price += 0
    elif 18 <= int(age[i]) <= 25:
        price += cost2
    elif int(age[i]) > 25:
        price += cost3
if tickets > 3:
    price = price/100*90     # Скидка если билетов больше 3
print(f'Общая стоимость билетов: {price}')
