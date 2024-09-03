# 1. Ітератори в Python
# Ітератори — це об'єкти, які можуть послідовно перебирати елементи контейнера
# (наприклад, списку або словника). 
# Будь-який об'єкт, який підтримує методи __iter__() і __next__(), може бути ітератором.


# 1. Приклади ��тераторів в Python
my_list = [1, 2, 3]
iterator = iter(my_list)  # Отримуємо ітератор

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3




# 2. Генератори в Python
# Генератори — це функції, які повертають ітератори і можуть призупиняти своє виконання, 
# зберігаючи свій стан (завдяки ключовому слову yield).

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
print(next(counter))  # 1
print(next(counter))  # 2






# 3. Замикання в Python
# Замикання (closures) — це функції, які «запам'ятовують» середовище, 
# в якому були створені, навіть якщо ця функція виконується поза межами цього середовища.


def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

hello_func = outer_function("Hello")
hello_func()  # Виведе "Hello"






# 4. Декоратори в Python
# Декоратори — це спеціальні функції, 
# які дозволяють модифікувати або розширювати поведінку інших функцій або методів.

def my_decorator(func):
    def wrapper():
        print("Щось виконується перед функцією.")
        func()
        print("Щось виконується після функції.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()




# 5. Декоратор @property в Python
# Декоратор @property дозволяє перетворити методи класу на властивості, 
# які можна використовувати як атрибути об'єкта.

class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Радіус не може бути від'ємним")
        self._radius = value

circle = Circle(5)
print(circle.radius)  # 5
circle.radius = 10
print(circle.radius)  # 10





# 6. Регулярні вирази в Python
# Регулярні вирази (regular expressions, або regex) 
# — це потужний інструмент для пошуку і обробки текстових шаблонів.


import re

pattern = r'\b[a-zA-Z]{4}\b'  # Шукає слова з чотирьох букв
text = "This is a test string with words like tree and bike."


matches = re.findall(pattern, text)
print(matches)  # ['This', 'test', 'tree', 'bike']

