jewel = ['золото', 'алмазы', 'серебро', 'сапфиры', 'бронза', 'рубины',
         'платина', 'изумруды', 'палладий', 'аметисты']


for i in range(0, 2):
    for index, value in enumerate(jewel[i::2]):
        index += 1
        print(index, value)
    print()


#Дополнительные переменные не нужны, просто в одном цикле переберите значения от 0 до 1 включительно и подставьте их в то место, где оно нужно в срезе
#там получится всего 5 строк кода
