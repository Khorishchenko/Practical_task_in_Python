# // 1. Числові типи даних

# Створіть змінні для цілого числа, числа з плаваючою комою та комплексного числа.
# Виведіть ці змінні на екран та їх типи.

valueInt = 10
valueFloat = 10.5


print(f"value int = {valueInt}, type is = " , type(valueInt))
print(f"value float = {valueFloat}, type is = ", type(valueFloat))






# 2. Математичні функції модуля math

# Використайте модуль math для обчислення квадратного кореня, експоненти та логарифму числа 10.
# Виведіть результати на екран.

import math

number = 10

sqrt_result = math.sqrt(number)
exp_result = math.exp(number)
log_result = math.log(number)

print(f"Квадратний корінь з {number}: {sqrt_result}")
print(f"Експонента з {number}: {exp_result}")
print(f"Логарифм з {number}: {log_result}")





# 3. Списки (list)

# Створіть список з п'яти елементів (різних типів даних).
# Додайте новий елемент до списку.
# Видаліть перший елемент.
# Виведіть остаточний список.

myList = [1, 10.4, 'j', "hello", "world"]

myList.append(100)

myList.pop(0)

print(f" My list is: {myList}")




# 4. Кортежі (tuple)
# Створіть кортеж з трьох елементів.
# Спробуйте змінити один з елементів кортежу (це повинно викликати помилку).
# Виведіть кортеж на екран.

mytuple = (1, 2, 3, 4)

# mytuple[1] = 12 // --- error

print(f"my tuple is : {mytuple}")




# 5. Рядки (str)
# Напишіть програму, яка приймає рядок від користувача.
# Виведіть довжину рядка, перший та останній символи.
# Перетворіть рядок у верхній та нижній регістри та виведіть їх на екран.

user_input = input("enter string: ")

print(f"size str is {len(user_input)}, first_element is {user_input[0]}, and last_element is {user_input[-1]}")

user_input = user_input.lower()
print(user_input)

user_input = user_input.upper()
print(user_input)
