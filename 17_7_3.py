per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = 100000
deposit = []
for key in per_cent.keys():
    deposit.append(int(money/100 * per_cent[key]))
print(f'deposit = {deposit}')
print(f'Максимальная сумма, которую вы можете заработать — {max(deposit)}')