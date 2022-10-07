# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
list = [random.randint(0,10) for i in range(random.randint(3,10))]
print(f"Specified list:\n{list}")
sum = 0
i = 1
while(i<len(list)):
    sum = sum + list[i]
    i=i+2
print(f"The sum of the list items in an odd position = {sum}")