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






# 1.1. Створення масиву з цілими числами ('i')

import array

numbers = array.array('i', [1, 2, 3, 4, 5])  # Масив тільки для цілих чисел
print(numbers)  # array('i', [1, 2, 3, 4, 5])
print(numbers[0])  # Виведе 1




# 1.2. Додавання та видалення елементів
numbers.append(6)  # Додає елемент 6 у кінець масиву
print(numbers)  # array('i', [1, 2, 3, 4, 5, 6])

numbers.insert(2, 10)  # Вставляє 10 на позицію з індексом 2
print(numbers)  # array('i', [1, 2, 10, 3, 4, 5, 6])

numbers.pop(3)  # Видаляє елемент на позиції 3 (число 3)
print(numbers)  # array('i', [1, 2, 10, 4, 5, 6])




# 1.3. Перебирання масиву
for num in numbers:
    print(num, end=' ')  # 1 2 10 4 5 6




# 1.4. Зміна значення елемента

numbers[1] = 20  # Замінює другий елемент (індекс 1)
print(numbers)  # array('i', [1, 20, 10, 4, 5, 6])















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


# 3.6.2 Потужні зрізи

list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)
# Присвоєння: list_2 = list_1 копіює назву масиву, а не його вміст. 
# По суті, дві назви (list_1 та list_2) ідентифікують одне і те ж саме місце в пам'яті комп'ютера. Зміна однієї з них впливає на іншу, і навпаки.


# На щастя, рішення у вас під рукою - воно називається зріз.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)



my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)




# 1. Розуміння списків дозволяє створювати нові списки з існуючих в лаконічний і елегантний спосіб. Синтаксис розуміння списку виглядає наступним чином:
# [expression for element in list if conditional]

row = []
WHITE_PAWN = '-'

for i in range(8):
    row.append(WHITE_PAWN)

row = [WHITE_PAWN for i in range(8)]


# Приклад №1:
squares = [x ** 2 for x in range(10)]
# Фрагмент створює десятиелементний список, заповнений квадратами десяти цілих чисел, починаючи з нуля (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)


# Приклад №2:
twos = [2 ** i for i in range(8)]
# Фрагмент створює восьмиелементний масив, що містить перші вісім степенів двійки (1, 2, 4, 8, 16, 32, 64, 128)


# Приклад №3:
odds = [x for x in squares if x % 2 != 0 ]
# Фрагмент формує список, який містить лише непарні елементи списку squares.





# 3.7.2 Двовимірні масиви
board = []
EMPTY = '*'

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)



# Оскільки списки можуть бути вкладеними, ми можемо скоротити створення дошки таким чином:
board = [[EMPTY for i in range(8)] for j in range(8)]
 
ROOK = '&'
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK



# Python не обмежує глибину включення списку в список. Нижче наведено приклад тривимірного масиву:
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
 
rooms[1][9][13] = True
rooms[0][4][1] = False


vacancy = 0
 
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
 



# end -- > https://acode.com.ua/list-python/











# Кортеж (tuple) в Python
# Кортеж в Python схожий на список. Різниця між ними полягає в тому, що ми не можемо змінити 
# елементи кортежу після присвоювання їм значень, тоді як елементи списку ми можемо змінити.

# ✅ tuple (кортеж)
# Що таке:
# Незмінна (immutable) послідовність.

# Легша за список.

# Використовується, коли дані не повинні змінюватися.

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






# # ✅ ЗАДАЧІ З tuple
# # Задача 1: Зберігання даних студента
# # Умова: Зберегти ім’я, вік та оцінку студента в кортежі. Вивести повідомлення.

student = ("Оля", 18, 93)
print(f"{student[0]} має {student[1]} років та оцінку {student[2]}")


# Список кортежів
# Умова: Є список товарів у вигляді (назва, ціна). Вивести всі назви.



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


# ✅ set (множина)
# Що таке:
# Немає дублікатів.

# Не зберігає порядок.

# Швидкий пошук.



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




# Додавання елемента до множини
# В Python метод add() використовується для додавання елемента до множини. Наприклад:

numbers = {21, 34, 54, 12}
 
print('Initial Set:',numbers)
 
# Використання методу add() 
numbers.add(32)
 
print('Updated Set:', numbers)

#  end -- > https://acode.com.ua/set-python/













# Словник (dict) в Python

# Словник в Python — це впорядкована колекція елементів, 
# яка зберігає їх у вигляді пари “ключ-значення”. 
# Ключ — це унікальний ідентифікатор, який пов’язаний із кожним значенням. 
# Наприклад, якщо нам потрібно зберегти інформацію про країни та їх столиці, 
# ми можемо створити словник з назвами країн як ключі та з назвами столиць як значеннями.


# Створення словника в Python
capital_city = {"Nepal": "Kathmandu", "Ukraine": "Kyiv", "Italy": "Rome"}
print(capital_city)


# Додавання елементів до словника
capital_city = {"Nepal": "Kathmandu", "Italy": "Rome"}
print("Initial Dictionary: ",capital_city)
 
capital_city["Japan"] = "Tokyo"
 
print("Updated Dictionary: ",capital_city)

# Зміна значень у словнику
# Ми також можемо використати [] для зміни значення, пов’язаного з певним ключем. Наприклад:

student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print("Initial Dictionary: ", student_id)
 
student_id[112] = "Stan"
 
print("Updated Dictionary: ", student_id)



# Видалення елементів зі словника
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
 
print("Initial Dictionary: ", student_id)
 
del student_id[111]
 
print("Updated Dictionary ", student_id)


#  end --> https://acode.com.ua/dictionary-python/