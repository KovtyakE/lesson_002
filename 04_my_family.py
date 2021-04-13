#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:
# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["Vova", "Alla", "Inna", "Matvey"]
print(my_family)
# список списков приблизителного роста членов вашей семьи
my_family_height = [
                        [my_family[0], 180],
                        [my_family[1], 165],
                        [my_family[2], 160],
                        [my_family[3], 155]
                    ]
# ['имя', рост],
choise = int(input('Введите, чьи данные хотите увидеть:\n 1 - Отец\n 2 - Мать\n 3 - Жена\n 4 - Брат:\n '))
print('значение списка:', my_family_height[choise-1])

# Выведите на консоль рост отца в формате
# Рост отца - ХХ см
if choise == 1:
    print('Рост отца: ', my_family_height[0][1], 'см')
elif choise == 2:
    print('Рост матери: ', my_family_height[1][1], 'см')
elif choise == 3:
    print('Рост жены: ', my_family_height[2][1], 'см')
elif choise == 4:
    print('Рост брата: ', my_family_height[3][1], 'см')
else: exit()

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
# Общий рост моей семьи - ХХ см
overall_height = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1] + 187
print(overall_height, 'см общий рост всей семьи')