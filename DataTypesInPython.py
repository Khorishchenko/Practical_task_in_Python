# Числові типи даних в Python
num1 = 6
print(num1, 'is of type', type(num1))
 
num2 = 7.34
print(num2, 'is of type', type(num2))
 
num3 = 3+5j
print(num3, 'is of type', type(num3))




# Системи числення
print(0b1101011)  # двійкова система числення, виведе 107
 
print(0o15)  # вісімкова система числення, виведе 13
 
print(0xFB + 0b10)  # шістнадцяткова система числення, виведе 253






# Перетворення числових типів даних в Python
# Явне перетворення числових типів даних

num1 = int(4.3)
print(num1)  # виведе 4
 
num2 = int(-3.7)
print(num2)  # виведе -3
 
num3 = float(6)
print(num3)  # виведе 6.0
 
num4 = complex('4+6j')
print(num4)  # виведе (4 + 6j)






# Модуль random в Python
import random
 
# Виводимо випадкове число з діапазону від 10 до 20
print(random.randrange(10, 20))
 
# Створюємо список елементів 
list1 = ['a', 'b', 'c', 'd', 'e']
 
# Виводимо випадковий елемент із списку list1
print(random.choice(list1))
 
# Перемішуємо список list1
random.shuffle(list1)
 
# Виводимо перемішаний список list1
print(list1)
 
# Виводимо випадкове число
print(random.random())







# Модуль math в Python
# Python пропонує модуль math для виконання різних математичних операцій, включаючи тригонометрію, 
# ймовірність та статистику, роботу з логарифмами тощо. Наприклад:

import math
 
print(math.pi)
 
print(math.cos(math.pi))
 
print(math.exp(10))
 
print(math.log10(1000))
 
print(math.sinh(1))
 
print(math.factorial(6))


# Математичні функції модуля math в Python
# https://acode.com.ua/mathematical-functions-python/











# Список (list) в Python
# Списки в Python використовуються для одночасного зберігання багатьох даних. 
# Список створюється шляхом розміщення елементів всередині квадратних дужок [], 
# розділених комами. Список може містити 
# будь-яку кількість елементів, і вони можуть бути різних типів (int, float, string тощо).



# Створення списку в Python

# Список із 3 цілих чисел
numbers = [1, 2, 5]
 
print(numbers)


# Список може містити будь-яку кількість 
# елементів і вони можуть бути різних типів (int, float, string тощо). 
# Наприклад:

# Порожній список
my_list = []
 
# Список із змішаними типами даних
my_list = [1, "Hello", 3.4]



# Доступ до елементів списку в Python
# В Python кожен елемент списку асоціюється з індексом. 
# Ми можемо отримати доступ до елементів масиву, використовуючи номер індексу (0, 1, 2,…). Наприклад:


languages = ["Python", "Swift", "C++"]
 
# Отримуємо доступ до елемента під індексом 0
print(languages[0])   # виведе Python
 
# Отримуємо доступ до елемента під індексом 2
print(languages[2])   # виведе C++





# Від’ємна індексація в Python
languages = ["Python", "Swift", "C++"]
 
# Отримуємо доступ до елемента під індексом 0
print(languages[-1])   # виведе C++
 
# Отримуємо доступ до елемента під індексом 2
print(languages[-3])   # виведе Python






# Зріз списку в Python
 
my_list = ['p','r','o','g','r','a','m','i','z']
 

# Виводимо "зрізані" елементи з 2 по 4 індекс
print(my_list[2:4])
 
# Виводимо "зрізані" елементи від індексу 5 і до кінця списку
print(my_list[5:])
 
# Виводимо всі елементи списку
print(my_list[:])



# Додавання елементів до списку в Python
# Метод append() додає елемент в кінець списку. Наприклад:
numbers = [21, 34, 54, 12]
 
print("Before Append:", numbers)
 
# Використання методу append()
numbers.append(32)
 
print("After Append:", numbers)


# end -- > https://acode.com.ua/list-python/










# Кортеж (tuple) в Python
# Кортеж в Python схожий на список. Різниця між ними полягає в тому, що ми не можемо змінити 
# елементи кортежу після присвоювання їм значень, тоді як елементи списку ми можемо змінити.


# Створення кортежу в Python

# Різні типи кортежів
 
# Порожній кортеж
my_tuple = ()
print(my_tuple)
 
# Кортеж, що містить цілі числа
my_tuple = (1, 2, 3)
print(my_tuple)
 
# Кортеж зі змішаними типами даних
my_tuple = (1, "Hello", 3.4)
print(my_tuple)
 
# Вкладений кортеж
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)


#  end -- > https://acode.com.ua/tuple-python/






# Рядки в Python
# Рядок — це послідовність символів. Наприклад, 
# "hello" — це рядок, що складається з набору символів: 'h', 'e', 'l', 'l' та 'o'.

# Створення рядка за допомогою подвійних лапок
string1 = "Python programming"
 
# Створення рядка за допомогою одинарних лапок
string1 = 'Python programming'


# Створення змінної рядкового типу
name = "Python"
print(name)
 
message = "I love Python."
print(message)


# Імутабельність рядків в Python

# Рядки в Python є іммутабельними. Це означає, що їх символи не можуть бути змінені. 
# Наприклад:

message = 'Hola Amigos'
# message[0] = 'H' # error !!!
print(message) 


# Однак, змінній можна присвоїти нове рядкове значення. Наприклад:
message = 'Hola Amigos'
 
# # Присвоюємо змінній message нове значення
message = 'Hello Friends'
print(message) # виведе "Hello Friends"

# end -- > https://acode.com.ua/strings-python/






# Абстракція списків (List Comprehension) в Python

# Приклади абстракції списків
# Припустимо, ми хочемо розділити літери слова human і додати їх як елементи списку. 
# Перше, що спадає на думку — це використати цикл for.

# Приклад №1: Ітерація по рядку за допомогою циклу for:

h_letters = []
 
for letter in 'human':
    h_letters.append(letter)
 
print(h_letters)


# Однак в Python є простіший спосіб розв’язати цю проблему — використати абстракцію списків.
# Приклад №2: Ітерація по рядку за допомогою абстракції списків:

h_letters = [ letter for letter in 'human' ]
print( h_letters)


# Абстракція списків vs. Лямбда-функції

# Приклад №3: Використання лямбда-функцій всередині списку:

letters = list(map(lambda x: x, 'human'))
print(letters)

# Вкладені цикли в абстракції списків
# Приклад №7: Транспонування матриці за допомогою циклів for:

transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
 
for i in range(len(matrix[0])):
    transposed_row = []
 
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
 
print(transposed)


# Приклад №8: Транспонування матриці за допомогою абстракції списків:
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)




# end --- > https://acode.com.ua/list-comprehension-python/










# Множина (set) в Python
# Множина (set) в Python — це набір унікальних даних. 
# Елементи множини не можуть дублюватися. Множина може містити будь-яку кількість елементів, 
# і вони можуть бути різних типів (int, float, кортеж, рядки тощо). 
# Але множина не може мати змінювані елементи, такі як списки, словники або інші множини. 
# Для створення множини всі елементи поміщають усередині фігурних дужок {}, розділених комами.


# Множина цілочисленного типу
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)
 
# Множина рядкового типу
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)
 
# Множина змішаного типу
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)




# Створення порожньої множини
empty_set = set()
 
# Створення порожнього словника
empty_dictionary = { }
 
# Перевірка типу даних empty_set
print('Data type of empty_set:', type(empty_set))
 
# Перевірка типу даних dictionary_set
print('Data type of empty_dictionary', type(empty_dictionary))