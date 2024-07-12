

# Файл — це контейнер для зберігання даних. Коли ми хочемо читати з файлу або записувати в нього, 
# нам потрібно спочатку його відкрити. Після того, 
# як ми закінчили читання/запис, нам потрібно закрити файл, щоб звільнити ресурси, пов’язані з ним.


# Відкриваємо файл у поточному каталозі
file1 = open("text.txt")

# За замовчуванням файли відкриті в режимі читання (не можуть бути змінені). Вищенаведений код рівнозначний:
# file1 = open("test.txt", "r")

# Читаємо файл
read_content = file1.read()
print(read_content)


# Закриваємо файл
file1.close()





# Обробка винятків у файлах

# Якщо під час виконання будь-якої операції з файлом виникає виняток, програма завершує виконання,
# не закриваючи при цьому файли. 
# Одним із рішень в цій ситуації є використання блоку try...finally.

try:
    file1 = open("text.txt", "r")
    read_content = file1.read()
    print(read_content)
 
finally:
    # Закриваємо файл
    file1.close()



# Використання синтаксису with…open
with open("text.txt", "r") as file1:
    read_content = file1.read()
    print(read_content)

# Примітка: Оскільки в цьому варіанті не потрібно турбуватися про закриття файлу, 
# рекомендується завжди використовувати синтаксис with...open.


# Запис у файл в Python

# При записі у файл необхідно пам’ятати дві речі:

#    Якщо ми намагаємося відкрити неіснуючий файл, створюється новий файл.

#    Якщо файл уже існує, його вміст видаляється, а до файлу додається новий вміст.



with open('text2.txt', 'w') as file2:
 
    # Виконуємо запис у файл test2.txt
    file2.write('Programming is Fun.')
    file2.write('Python for beginners')


#  end -- > https://acode.com.ua/file-operations-python/















# Робота з каталогами в Python
# Каталог — це набір файлів та підкаталогів. Каталог усередині каталогу називається підкаталогом. 
# В Python є модуль os, який надає багато корисних методів для роботи з каталогами та файлами.

# Ми можемо вивести поточний каталог за допомогою методу getcwd() модуля os. 
# Цей метод повертає поточний робочий каталог як рядок. Наприклад:
import os
 
print(os.getcwd())



# Створення нового каталогу в Python
# В Python ми можемо створити новий каталог за допомогою методу mkdir(). Цей метод приймає шлях до нового каталогу. 
# Якщо повний шлях не вказано, новий каталог створюється у поточному робочому каталозі.



os.mkdir('test')
 
os.listdir()
['test']






# Перейменування каталогу чи файлу в Python

import os
 
os.listdir()
['test']
 
# Перейменування каталогу
os.rename('test','new_one')
 
os.listdir()
['new_one']






# Видалення каталогу чи файлу в Python


# Спочатку скористаємося методом remove() для видалення файлу:
import os
 
# Видалення файлу "myfile.txt"
os.remove("myfile.txt")






# Тепер скористаємося методом rmdir() для видалення порожнього каталогу:
import os
 
# Видалення порожнього каталогу "mydir"
os.rmdir("mydir")





# Щоб видалити каталог, ми можемо використати метод rmtree() з модуля shutil. Наприклад:
import shutil
 
# Видалення каталогу "mydir" та його вмісту
shutil.rmtree("mydir")




















# Винятки в Python
# Виняток — це несподівана ситуація, яка відбувається під час виконання програми. Наприклад:

# Помилки, що виникають під час виконання програми 
# (після проходження синтаксичної перевірки), називаються винятками або логічними помилками.

# Наприклад, вони виникають, коли ми:

#    намагаємося відкрити неіснуючий файл — генерується виняток FileNotFoundError;

#    намагаємося ділити на нуль — генерується виняток ZeroDivisionError;

#    намагаємося імпортувати неіснуючий модуль — генерується виняток ImportError.


# Помилки та винятки в Python
# Помилками зазвичай є помилки компіляції, синтаксичні помилки, помилки у логічній частині коду, несумісність бібліотек, нескінченна рекурсія тощо.

# Винятки можуть бути спіймані та оброблені програмою.



# Ми можемо переглянути всі вбудовані винятки за допомогою функції local() наступним чином:
print(dir(locals()['__builtins__']))

#  end --> https://acode.com.ua/exceptions-python/







# Обробка винятків в Python

# Конструкція try…except в Python

try:
    pass
    # Код, який може згенерувати виняток
except:
    pass
    # Код для виконання у разі генерації винятку




# Приклад обробки винятку за допомогою try...except:

try:
    numerator = 10
    denominator = 0
 
    result = numerator/denominator
 
    print(result)
 
except:
    print("Error: Denominator cannot be 0.")




# Для кожного блоку try може існувати від нуля і більше блоків except. 
# Декілька блоків except дозволяють обробляти кожен виняток по-різному.

try:
    even_numbers = [2,4,6,8]
    print(even_numbers[5])
 
except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")




# Конструкція try з умовою else в Python

# У деяких ситуаціях може знадобитися виконати певний блок коду, якщо код всередині try виконається без помилок. 
# Для таких випадків використовується необов’язкове ключове слово else разом з оператором try.


try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
 
except:
    print("Not an even number!")
 
else:
    reciprocal = 1/num
    print(reciprocal)






# Конструкція try…finally в Python
# В Python блок finally виконується завжди, незалежно від того, генерується виняток чи ні. 
# Блок finally є необов’язковим. 
# І для кожного блоку try може бути лише один блок finally. Наприклад:

try:
    numerator = 10
    denominator = 0
 
    result = numerator/denominator
 
    print(result)
 
except:
    print("Error: Denominator cannot be 0.")
    
finally:
    print("This is finally block.")












# Користувацькі винятки в Python
# Визначення користувацьких винятків
# В Python ми можемо визначити користувацькі винятки, 
# створивши новий клас, який буде дочірнім вбудованому класу Exception.

class CustomError(Exception):
    ...
    pass
 
try:
   ...
 
except CustomError:
    ...




def sum():
    ...



from typing import List

def process_items(items: List[int]) -> None:
    """
    Ця функція приймає список цілих чисел і не повертає значення.
    
    :param items: Список цілих чисел
    :return: None
    """
    for item in items:
        print(item)

# def process_items(items: List[int]) -> None::
# def: Ключове слово для визначення нової функції.
# process_items: Ім'я функції.
# items: Аргумент функції.
# List[int]: Анотація типу для аргументу items, яка вказує,
# що items має бути списком (List) з елементами типу int (цілі числа).
# -> None: Анотація типу для повертаємого значення функції, яка вказує, 
# що ця функція не повертає значення (повертає None).








# Розглянемо приклад використання користувацького винятку в Python:

# Визначаємо користувацький виняток
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass
 
# Потрібно вгадати це число
number = 18
 
try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
        
except InvalidAgeException:
    print("Exception occurred: Invalid Age")



# raise в Python використовується для генерації винятків.
# Це ключове слово дозволяє вам створити власний виняток або повторно підняти вже існуючий. 
# Ось декілька прикладів використання raise:

class MyCustomError(Exception):
    pass

def do_something():
    raise MyCustomError("Something went wrong")

try:
    do_something()
except MyCustomError as e:
    print(e)  # Виведе: Something went wrong





# Кастомізація класів винятків

# Щоб дізнатися про налаштування (кастомізацію) класів винятків, 
# необхідно мати базові знання про об’єктно-орієнтоване програмування. Наприклад::


class SalaryNotInRangeError(Exception):
    """Виняток, викликаний помилками у вхідному значенні salary
 
    Атрибути:
        salary -- значення salary, яке викликало помилку
        message -- пояснення помилки
    """
 
    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)
 
salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)