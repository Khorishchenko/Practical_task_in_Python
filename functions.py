print("hello world")

# Визначення функції з двома параметрами
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ",sum)
 
# Виклик функції з вказанням двох аргументів
add_numbers(5, 4)



# Визначення функції
def get_square(num):
    return num * num
 
for i in range(3):
    # Виклик функції
    result = get_square(i)
    print('Square of',i, '=',result)




def add_numbers( a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)
 
 
# Виклик функції з 2 аргументами
add_numbers(2, 3)
 
# Виклик функції з 1 аргументом
add_numbers(a = 2)
 
# Виклик функції без надання аргументів
add_numbers()




def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)
 
display_info(last_name = 'Cartman', first_name = 'Eric')

# Відповідно, аргумент first_name у виклику функції стає параметром first_name у визначенні функції. 
# Так само аргумент last_name у виклику функції стає параметром last_name у визначенні функції.

# У таких сценаріях порядок надання аргументів немає значення.





# Довільні аргументи в Python

# Довільні аргументи дозволяють передавати різну кількість значень під час виклику функції. 
# Для вказівки даного типу аргументів використовується зірочка (*) перед ім’ям параметра у визначенні функції. Наприклад:


def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)
 
# Виклик функції з 3 аргументами
find_sum(1, 2, 3)
 
# Виклик функції з 2 аргументами
find_sum(4, 9)



# Лямбда (анонімні функції) в Python

greet = lambda : print('Hello, World!')

# Викликаємо лямбда-функцію
greet()


# Лямбда-функція з аргументами в Python
# Лямбда-функція, яка приймає 1 аргумент
greet_user = lambda name : print('Hey there,', name)
 
# Виклик лямбда-функції
greet_user('Delilah')



# Програма подвоєння значень кожного елемента списку за допомогою функції map()
 
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)




# Як використовувати лямбда-функцію з filter()?
# Програма фільтрації лише парних елементів зі списку
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
 
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
 
print(new_list)



# Ключове слово nonlocal використовується для створення нелокальних змінних. Наприклад:
# Зовнішня функція 
def outer():
    message = 'local'
 
    # Вкладена функція
    def inner():
 
        # Оголошуємо нелокальну змінну
        nonlocal message
 
        message = 'nonlocal'
        print("inner:", message)
 
    inner()
    print("outer:", message)
 
outer()




# Використання ключового слова global у вкладених функціях
def outer_function():
    num = 20
 
    def inner_function():
        global num
        num = 25
    
    print("Before calling inner_function(): ", num)
    inner_function()
    print("After calling inner_function(): ", num)
 
outer_function()
print("Outside both function: ", num)



# Що таке модуль?
# Модуль — це файл, який містить код для виконання певного завдання. Модуль може містити змінні, функції, класи тощо.

# Давайте створимо модуль. Напишіть наступний код та збережіть його як файл example.py:

import example


example.add(4,5) # результатом буде 9


# Імпорт модулів із Cтандартної бібліотеки Python
# Імпортуємо модуль math зі Стандартної бібліотеки Python
import math
 
# Використовуємо math.pi для отримання значення числа Пі
print("The value of pi is", math.pi)




# Перейменування модуля в Python
# Імпортуємо модуль, а потім перейменовуємо його
import math as m
 
print(m.pi)


# Імпортуємо тільки pi з модуля math
from math import pi
 
print(pi)


# В Python ми можемо імпортувати всі імена (визначення) із модуля, використовуючи наступну конструкцію:

# Імпортуємо всі імена з модуля math
from math import *
 
print("The value of pi is", pi)



# Пакет — це каталог (папка), який може містити інші каталоги або модулі. Модуль — це файл із вихідним кодом, який має розширення .py. 
# Пакети використовуються для формування простору імен, що дозволяє працювати з модулями через вказування рівня вкладеності 
# (за допомогою оператора .). Для імпортування пакетів використовується той самий синтаксис, що й для роботи з модулями.


import game.Level.start
game.Level.start.select_difficulty(2)
from game.Level import start

