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


my_tuple = (1, "hello", 3.14)

# Спроба змінити елемент кортежу (викличе помилку)
try:
    my_tuple[1] = "new value"
except TypeError as e:
    print(f"Помилка: {e}")

print("Кортеж:", my_tuple)




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


# 6. Абстракція списків (List Comprehension)
# Напишіть програму, яка створює список квадратів чисел від 1 до 10,
# використовуючи абстракцію списків. Виведіть результат на екран.

squares = [x**2 for x in range(1, 11)]
print("Список квадратів чисел від 1 до 10:", squares)





# 7. Робота з Множинами (set):
# Створити дві множини, set1 та set2, і заповнити їх випадковими значеннями.
# Вивести на екран елементи, які присутні в обох множинах.
# Вивести на екран елементи, які є тільки в set1, але не в set2.
# Об'єднати множини set1 та set2 і вивести результат.

import random

empty_set_one = set()
empty_set_two = set()

for element in range(10):
    empty_set_one.add(random.randrange(0, 10))
    empty_set_two.add(random.randrange(0, 10))

print(empty_set_one)
print(empty_set_two)

print('Intersection using intersection():', empty_set_one.intersection(empty_set_one))
print('Difference using difference():', empty_set_one.difference(empty_set_two))

print('Union using union():', empty_set_one.union(empty_set_two))







# 8. Робота зі Словниками (dict):
# Створити словник, який зберігає імена та вік кількох людей.
# Додати до словника нову пару ключ-значення.
# Видалити зі словника елемент за заданим ключем.
# Перебрати словник і вивести кожне ім'я разом із віком.


dicts = {
    "name": "John",
    "age": 25,
    "city": "Kyiv"
}

dicts["addres"] = "vailon"

print(f"our dic: {dicts}")

key = input("enter key for delete element: ")

del dicts[key]

print(f"our dic: {dicts}")