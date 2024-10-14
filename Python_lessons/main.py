# def main():
#     print("Hello, world!")

# if __name__ == '__main__':
#     main()




import math
import os
import random
import re
import sys

# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

# if __name__ == '__main__':
#     n = int(input().strip())
    
#     if n % 2 == 1:
#         print('Weird')
#     else:
#         if 2 <= n <= 5:
#             print('Not Weird')
#         elif 6 <= n <= 20:
#             print('Weird')
#         else:
#             print('Not Weird')


# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
    
# print(int(a / b))
# print(float(a / b))



# Input the values of a, b, and m
# a = int(input())  # first integer
# b = int(input())  # second integer
# m = int(input())  # third integer (modulus)

# Print the result of a^b
# print(pow(a, b))

# # Print the result of (a^b) % m
# print(pow(a, b, m))


# У цьому завданні потрібно прочитати чотири числа \(a\), \(b\), \(c\), \(d\) і вивести результат обчислення виразу \(a^b + c^d\). 
# Використаємо Python, оскільки він підтримує роботу з дуже великими цілими числами.

### Приклад коду для цього завдання:
# # Введення чотирьох чисел
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# # Обчислення результату
# result = a**b + c**d

# # Виведення результату
# print(result)


### Пояснення:
# 1. Ми читаємо чотири цілі числа зі стандартного введення за допомогою `input()` та перетворюємо їх на тип `int`.
# 2. Обчислюємо вираз \(a^b + c^d\), використовуючи оператор ** (степінь) для піднесення до степеня.
# 3. Виводимо результат на екран за допомогою `print()`.

### Приклад:

# **Введення:**
# ```
# 9
# 29
# 7
# 27
# ```

# **Виведення:**
# ```
# 4710194409608608369201743232
# ```

# Така задача демонструє можливість Python оперувати дуже великими числами без обмежень на розмір.

# if __name__ == '__main__':
#     a = int(input())
#     try:
#         if a < 0:
#             print("Пожалуйста, введите положительное целое число.")
#         else:
#             for i in range( a ):
#                 print(*range(1, i))
#     except ValueError:
#         print("Ошибка: пожалуйста, введите корректное целое число.")

# 2. **Неоптимальные вложенные циклы:** Вложенные циклы  for  могут привести к значительным затратам по времени, особенно если  a  велико. 
# Вместо этого можно использовать более эффективные методы для достижения желаемого результата. 
# - Убран второй цикл, и вместо него используется распаковка  print(*range(i)) , что делает вывод более эффективным.



# for i in range(1, int(input())): 
#     print(i * (10**i // 9))


# import asyncio

# async def task1():
#     print("Задача 1 почалася")
#     await asyncio.sleep(2)  # Асинхронна пауза на 2 секунди
#     print("Задача 1 завершена")

# async def task2():
#     print("Задача 2 почалася")
#     await asyncio.sleep(1)  # Асинхронна пауза на 1 секунду
#     print("Задача 2 завершена")

# async def main():
#     await asyncio.gather(task1(), task2())  # Виконуємо задачі одночасно

# # Запускаємо головну функцію
# asyncio.run(main())



import numpy


def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(arr, dtype=int)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)