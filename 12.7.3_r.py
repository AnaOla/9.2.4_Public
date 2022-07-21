per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent_list = list(map(float, per_cent.values()))
money = int(input('Введите сумму:'))
deposite = [round(i/100*money) for i in per_cent_list]
print(deposite)
print('Максимальная сумма, которую вы можете заработать —','',max(deposite))