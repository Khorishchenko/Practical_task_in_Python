# У Python немає структур даних у класичному сенсі, як у мові C або C++, де існує ключове слово struct для створення структур. 
# Однак Python надає декілька способів створення структурованих даних за допомогою вбудованих типів та інструментів, таких як:




# 1. Кортежі (Tuples):
# Кортежі — це незмінювані структури, які можуть містити елементи різних типів.


person = ("John", 25, "Engineer")
print(person[0])  # Output: John



# 2. Словники (Dictionaries):
# Словники дозволяють зберігати дані у форматі ключ-значення.
person = {
    "name": "John",
    "age": 25,
    "profession": "Engineer"
}
print(person["name"])  # Output: John



# 3. NamedTuples (Іменовані кортежі):
# Це покращена версія кортежів, де елементи можна звертати за іменами полів.


from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'profession'])
person = Person(name="John", age=25, profession="Engineer")
print(person.name)  # Output: John




# 5. Dataclasses:
# З Python 3.7 з'явився модуль dataclasses, який дозволяє створювати класи 
# для зберігання даних без необхідності вручну визначати конструктори чи інші методи.

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    profession: str

person = Person(name="John", age=25, profession="Engineer")
print(person.name)  # Output: John



# Висновок:
# У Python немає класичних структур як у C або C++, 
# але існують альтернативні підходи для створення структурованих даних, 
# таких як кортежі, словники, іменовані кортежі, класи та dataclasses.