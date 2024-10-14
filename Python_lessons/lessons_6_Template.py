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