'''
charly = pet.Pet('Cake', datetime.date(2000, 12, 22), 13500, 600, True, True, datetime.date(2011, 11, 11), datetime.date(2012, 12, 12))

print(charly)

add_db = Pet(name=charly.name, birth_date=charly.birth_date, feed_weight=charly.feed_weight,
             vaccination=charly.vaccination, tick_protect=charly.tick_protect, vaccination_date=charly.vaccination_date,
             tick_protect_date=charly.tick_protect_date)

session.add(add_db)
session.commit()



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

#print(charly.age())

print(charly)


print('====== ТЕСТ ДОБАВЛЕНИЯ В БАЗУ ДАННЫХ ======')
new_pet = Pet(name='Монти', birth_date=datetime.date(2015, 5, 26))
session.add(new_pet)
session.commit()
print('====== OK ======')

print('====== ТЕСТ ЗАПРОСА К БД ======')
for r in session.query(Pet, Pet.name).all():
    print(r.Pet, r.name)
print('====== OK ======')
'''
