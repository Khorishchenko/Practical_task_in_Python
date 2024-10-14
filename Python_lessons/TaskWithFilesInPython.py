

# 1. Робота з файлами в Python. Читання та запис

# Напишіть програму, яка створює файл з ім'ям "example.txt" і записує в нього наступний текст:

'''Копіювати код
Це приклад тексту.
Другий рядок тексту.'''

# Напишіть функцію, яка читає вміст файлу "example.txt" і виводить його на екран.
# Додайте в кінець файлу "example.txt" ще один рядок тексту: "Третій рядок тексту."

with open(r'example.txt', 'w') as file:
    file.write(
''' Копіювати код
    Це приклад тексту.
    Другий рядок тексту
    ''')
    

def appendStr(file_name, str):
    with open(file_name, 'a') as file:
        file.write(str + '\n')

def readFromFile(file_name):
    with open(file_name, 'r') as file:
        for line in file.readlines():
            print(line)


appendStr('example.txt', 'Третій рядок тексту.')
readFromFile('example.txt')





# 2. Робота з каталогами в Python
# Завдання:

# Напишіть програму, яка створює новий каталог з ім'ям "test_dir".
# Створіть кілька файлів у цьому каталозі.
# Напишіть функцію, яка виводить список усіх файлів у каталозі "test_dir".
# Підказка:

# Використовуйте модулі os та os.path.


import os

directory = "test_dir"

if not os.path.exists(directory):
    os.makedirs(directory)

filenames = ["file1.txt", "file2.txt", "file3.txt"] 

for i, filename in enumerate(filenames, start=1):
    filepath = os.path.join(directory, filename)
    if os.path.exists(directory):  # Проверка наличия каталога
        with open(filepath, 'a') as file:  # Используем режим 'a' для добавления в файл, а не перезаписи
            file.write(f"Это файл file{i}.txt\n")
    else:
        print(f"Каталог {directory} не существует.")







# 3. Винятки в Python
# Завдання:

# Напишіть програму, яка запитує у користувача число і ділить 100 на це число.
# Додайте обробку винятків, щоб уникнути помилки ділення на нуль.


numbers = int(input("enter number: "))

try:
    result = 100 / numbers
    print(result)
except ZeroDivisionError:
    print("Error: Denominator cannot be 0.")








# 4. Обробка винятків в Python
# Напишіть функцію, яка приймає два аргументи: ім'я файлу та рядок тексту.
# Спробуйте відкрити файл для запису і записати в нього текст.
# Додайте обробку винятків для випадків, коли файл не може бути відкритий або записаний (наприклад, через відсутність прав доступу).

# Підказка:
# Використовуйте блоки try, except, else та finally.

def openfile(filename, text):
    try:
        with open(filename, 'a') as file:
            file.write(text + '\n')
    except FileNotFoundError:
        raise Exception("Ошибка открытия файла")

openfile("example.txt", "Hello World")








# 5. Користувацькі винятки в Python
# Завдання:

# Створіть власний клас винятку CustomError, який наслідує від Exception.
# Напишіть функцію, яка приймає число і піднімає CustomError, якщо число від'ємне.
# Напишіть програму, яка викликає цю функцію і обробляє піднятий виняток.
# Підказка:

# Використовуйте ключове слово raise для підняття винятку та блоки try/except для його обробки.


class CustomsError( Exception ):
    def __init__( self, text_error ):
        super().__init__( text_error )


def checkPositive( number ):
    if number < 0:
        raise CustomsError("Number is negative")
    else:
        print( f"number is { number }" )


try:
    checkPositive( 10 )
except CustomsError as error:
    print( error )