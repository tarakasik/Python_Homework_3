# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний
# элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
list = [random.randint(0,10) for i in range(random.randint(3,10))]
print(f"Specified list:\n{list}")
i = 0
array = []
while(i<len(list)/2):
    array.append(list[i]*list[len(list)-(i+1)])
    i+=1
print(array)