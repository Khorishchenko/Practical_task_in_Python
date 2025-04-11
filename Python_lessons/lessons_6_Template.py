# В Python немає шаблонних функцій і класів у тому ж сенсі, що вони є в C++ або Java. 
# Проте Python підтримує типи узагальнення (generics) через бібліотеку typing, що дозволяє створювати функції та класи, які працюють з різними типами даних.




# Узагальнені функції
# Для створення узагальнених функцій в Python, можна використовувати модуль typing. 
# Наприклад, ось як можна створити узагальнену функцію, яка працює з будь-яким типом даних:

from typing import TypeVar

T = TypeVar('T')

def get_first_element(data: list[T]) -> T:
    return data[0]

# Використання узагальненої функції
print(get_first_element([1, 2, 3]))       # Виведе: 1
print(get_first_element(['a', 'b', 'c'])) # Виведе: 'a'







# Узагальнені класи
# Так само, можна створювати узагальнені класи, використовуючи модуль typing. Ось приклад узагальненого класу:

from typing import Generic, TypeVar

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self._items = []

    def push(self, item: T):
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

# Використання узагальненого класу
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
print(int_stack.pop())  # Виведе: 2

str_stack = Stack[str]()
str_stack.push('a')
str_stack.push('b')
print(str_stack.pop())  # Виведе: 'b'




#====================================================================================================================================================
# Generics
# Дженерики (Generics) — це концепція, яка дозволяє створювати узагальнені функції, 
# класи або структури даних, які можуть працювати з різними типами, не вимагаючи конкретизації типу 
# заздалегідь. У Python дженерики дозволяють визначати функції або класи, які можуть працювати з різними типами
# об'єктів, 
# зберігаючи при цьому інформацію про типи для статичного аналізу.
from collections.abc import Sequence
from typing import TypeVar


def first[T](l: Sequence[T]) -> T:  # Function is generic over the TypeVar "T"
    return l[0]


U = TypeVar('U')                  # Declare type variable "U"

def second(l: Sequence[U]) -> U:  # Function is generic over the TypeVar "U"
    return l[1]







# 1. Створення дженеричних функцій
# Функції, що працюють з будь-якими типами, 
# можуть використовуватися разом із typing.Generic і параметрами типу, як у наступному прикладі:


from typing import TypeVar


# Оголошуємо TypeVar, який представляє узагальнений тип
T = TypeVar('T')

# Дженерична функція, яка працює з будь-яким типом T
def identity(value: T) -> T:
    return value

print(identity(42))        # Працює з типом int
print(identity("Hello"))    # Працює з типом str
print(identity([1, 2, 3]))  # Працює з типом list




# 2. Дженеричні класи
from typing import TypeVar, Generic

# Оголошуємо узагальнений тип
T = TypeVar('T')

# Дженеричний клас, який працює з будь-яким типом T
class Box(Generic[T]):
    def __init__(self, content: T):
        self.content = content
    
    def get_content(self) -> T:
        return self.content

# Приклад використання дженеричного класу
box1 = Box(123)        # Працює з типом int
box2 = Box("text")     # Працює з типом str

print(box1.get_content())  # Output: 123
print(box2.get_content())  # Output: text






# 3. Дженерики з обмеженням типу
# Іноді потрібно обмежити дженерик лише до певних типів. 
# Це можна зробити, використовуючи параметри типу з обмеженням.

from typing import TypeVar

# Обмежуємо тип до числових типів (int, float)
T = TypeVar('T', int, float)

def add_numbers(a: T, b: T) -> T:
    return a + b

print(add_numbers(3, 4))    # Працює з int
print(add_numbers(5.5, 2.3))  # Працює з float