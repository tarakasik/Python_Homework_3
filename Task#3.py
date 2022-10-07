# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


import random
list = [round(random.random()*random.randint(0, 100), 2)
        for i in range(random.randint(3, 10))]
print(f"Specified list:\n{list}")
array = []
i = 0
while (i < len(list)):
    array.append((round(list[i] % 1, 2)))
    i += 1
print(
    f"The minimum value of the list items:\n{round(max(array)-min(array),2)}")
