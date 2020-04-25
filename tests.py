import pet, time

charly = pet.Pet('Чарли', '26.04.2015')

print(f'Кличка: {charly.name}', f'День рождения: {charly.birth_date}')

print(f'Количество корма: {charly.feed_weight}', f'Потребление в день: {charly.feed_in_day}')
print('Покупаю 15 кг корма...')

charly.buy_feed(7500)
charly.feed_in_day = 600
print(f'Количество корма: {charly.feed_weight}', f'Потребление в день: {charly.feed_in_day}')
print(f'При суточном потреблении 600 г корма хватат на {charly.calculate_feed()} дней')
print('Есть ли прививки?')

if charly.vaccination:
    print('Есть')
else:
    print('Прививок нет!')

print('Делаю прививку...')

print('Есть ли прививки?')

charly.vaccination=True
if charly.vaccination:
    print('Есть')
else:
    print('Прививок нет!')

print('Защищен ли от клещей?')



while charly.feed_weight >= charly.feed_in_day:
    print(f'Осталось {charly.feed_weight / 1000} кг корма')
    print(f'Этого хватит на {charly.calculate_feed()} дней')
    charly.feed_weight -= charly.feed_in_day

print(charly.age())