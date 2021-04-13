#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.
lamp_code = goods['Лампа']
lamp_position = store[lamp_code][0]
lamp_quantity = lamp_position['quantity']
lamp_price = lamp_position['price']
lamp_cost = lamp_quantity * lamp_price
print('Всего ламп: ', lamp_quantity, '\nЦена лампы: ', lamp_price, ' руб.\nОбщая стоимость всех ламп: ',
      lamp_cost, ' руб.\n', sep='')

table_code = goods['Стол']
table_position_1 = store[table_code][0]
table_position_2 = store[table_code][1]
table_quantity_1 = table_position_1['quantity']
table_quantity_2 = table_position_2['quantity']
table_price_1 = table_position_1['price']
table_price_2 = table_position_2['price']
table_cost_1 = table_quantity_1 * table_price_1
table_cost_2 = table_quantity_2 * table_price_2
table_overall_cost = table_cost_1 + table_cost_2
print('Всего столов: ', table_quantity_1, ' одного типа и ', table_quantity_2, ' другого типа\n',
      'Цена столов: ', table_price_1, ' руб. одного типа и ', table_price_2, ' руб. другого типа\n',
      'Стоимость столов: ', table_cost_1, ' руб. одного типа и ', table_cost_2, ' руб. второго типа\n',
      'Общая стоимость всех столов: ', table_overall_cost, ' руб.\n', sep='')

sofa_code = goods['Диван']
sofa_position_1 = store[sofa_code][0]
sofa_position_2 = store[sofa_code][1]
sofa_quantity = sofa_position_1['quantity'] + sofa_position_2['quantity']
sofa_price_1 = sofa_position_1['price']
sofa_price_2 = sofa_position_2['price']
sofa_cost_1 = sofa_position_1['quantity'] * sofa_price_1
sofa_cost_2 = sofa_position_2['quantity'] * sofa_price_2
sofa_overall_cost = sofa_cost_1 + sofa_cost_2
print('Всего диванов: ', sofa_quantity, '\n',
      'Общая стоимость всех диванов: ', sofa_overall_cost, ' руб.\n', sep='')

chair_code = goods['Стул']
chair_position_1 = store[chair_code][0]
chair_position_2 = store[chair_code][1]
chair_position_3 = store[chair_code][2]
chair_quantity = chair_position_1['quantity'] + chair_position_2['quantity'] + chair_position_3['quantity']
chair_price_1 = chair_position_1['price']
chair_price_2 = chair_position_2['price']
chair_price_3 = chair_position_3['price']
chair_cost_1 = chair_position_1['quantity'] * chair_price_1
chair_cost_2 = chair_position_2['quantity'] * chair_price_2
chair_cost_3 = chair_position_3['quantity'] * chair_price_3
chair_overall_cost = chair_cost_1 + chair_cost_2 + chair_cost_3
print('Всего стульев: ', chair_quantity, '\n',
      'Общая стоимость всех стульев: ', chair_overall_cost, ' руб.\n', sep='')