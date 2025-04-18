import random

# # Лямбда (анонімні функції) в Python

# lambda аргументи: вираз

# Як це працює:
# lambda — ключове слово, яке починає визначення анонімної функції.
# аргументи — як у звичайної функції.
# вираз — один вираз (не блок коду!), який обчислюється й повертається.




# myFunc = lambda x, y: x * y
# print(myFunc(5, 5))  # 10


# # def f(x):
# #     return x * 2

# print(myFunc(10, 10))

def funUniversal(x, y, myLambda):
    print(myLambda(x, y))

    # result = 0
    # if (charValue == '-'):
    #     result = x - y
    # elif (charValue == '+'):
    #     result = x + y
    # elif (charValue == '*'):
    #     result = x * y
    # elif (charValue == '/'):
    #     result = x / y
    # elif (charValue == '**'):
    #     result = x ** y
    # else:
    #     result = 0

    # myList.append(result)
   

greet = lambda : print('Hello, World!')

Myelse = lambda : print('else')

Myelse()

print("else")

# # # Викликаємо лямбда-функцію
funUniversal(10, 20, lambda x, y: x + y)
funUniversal(10, 20, lambda x, y: x - y)
funUniversal(10, 20, lambda x, y: x * y)
funUniversal(10, 20, lambda x, y: x / y)
funUniversal(10, 20, lambda x, y: x ** y)
funUniversal(10, 20, lambda x, y: x == y)







# # Лямбда-функція з аргументами в Python
# # Лямбда-функція, яка приймає 1 аргумент

greet_user = lambda name : print('Hey there,', name)

def hello(name):
    print('Hey there,', name)

# # Виклик лямбда-функції
greet_user('Delilah')
hello("Sergii")



# 1. Сортування за довжиною рядків
words = ['banana', 'apple', 'kiwi']
words.sort(key=lambda x: len(x))
print(words) 



# # # 4. Сума двох чисел
add = lambda a, b: a + b
print(add(5, 3)) 




#================================================================
# Задача 4: Перевір, чи число більше 10
# Умова:
# Є число. Перевір, чи воно більше 10, за допомогою lambda.





#================================================================
# 1. Перевірка пароля
# Напишіть функцію check_password(password), яка приймає рядок і перевіряє:

# довжина не менше 8 символів,

# містить хоча б одну цифру,

# містить хоча б одну велику літеру.
# Функція має повертати True, якщо пароль надійний, і False в іншому випадку.

# char.isdigit(): and char.isupper()









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



# # Множина цілочисленного типу
# student_id = {112, 114, 116, 118, 115}
# print('Student ID:', student_id)
 
# # Множина рядкового типу
# vowel_letters = {'a', 'e', 'i', 'o', 'u'}
# print('Vowel Letters:', vowel_letters)
 
# # Множина змішаного типу
# mixed_set = {'Hello', 101, -2, 'Bye'}
# print('Set of mixed data types:', mixed_set)




# # Створення порожньої множини
# empty_set = set()
 
# # Створення порожнього словника
# empty_dictionary = { }
 
# # Перевірка типу даних empty_set
# print('Data type of empty_set:', type(empty_set))
 
# # Перевірка типу даних dictionary_set
# print('Data type of empty_dictionary', type(empty_dictionary))




# # Додавання елемента до множини
# # В Python метод add() використовується для додавання елемента до множини. Наприклад:

# numbers = {21, 34, 54, 12}
 
# print('Initial Set:',numbers)
 
# # Використання методу add() 
# numbers.add(32)
 
# print('Updated Set:', numbers)

#  end -- > https://acode.com.ua/set-python/




# ✅ ЗАДАЧІ З set
# Умова: Знайти унікальні імена зі списку з повторами.
# names = ["Anna", "Oleh", "Anna", "Maksym", "Oleh"]
# unique_names = set(names)
# print(unique_names)  # {'Anna', 'Oleh', 'Maksym'}











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
# my_tuple = ()
# print(my_tuple)
 
# # Кортеж, що містить цілі числа
# my_tuple = (1, 2, 3)
# print(my_tuple)
 
# # Кортеж зі змішаними типами даних
# my_tuple = (1, "Hello", 3.4)
# print(my_tuple)
 
# # Вкладений кортеж
# my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# print(my_tuple)






# # ✅ ЗАДАЧІ З tuple
# # Задача 1: Зберігання даних студента
# # Умова: Зберегти ім’я, вік та оцінку студента в кортежі. Вивести повідомлення.

# student = ("Оля", 18, 93)
# print(f"{student[0]} має {student[1]} років та оцінку {student[2]}")


# Список кортежів
# Умова: Є список товарів у вигляді (назва, ціна). Вивести всі назви.
