# Вбудовані функції в Python






# Функція abs() в Python
# Функція abs() повертає абсолютне значення вказаного числа. Якщо число є комплексним, функція abs() повертає його величину. 
# Наприклад:

number = -20
 
absolute_number = abs(number)
print(absolute_number)











# Функція any() в Python
# Функція any() повертає True, якщо хоча б один з елементів ітерованого об’єкта дорівнює True. Наприклад:

boolean_list = ['True', 'False', 'True']
 
# Перевірка, чи дорівнює елемент True
result = any(boolean_list)
print(result)


# True, оскільки елементи 1,3 та 4 дорівнюють True
l = [1, 3, 4, 0]
print(any(l))
 
# False, оскільки обидва елементи дорівнюють False
l = [0, False]
print(any(l))
 
# True, оскільки 5 дорівнює True
l = [0, False, 5]
print(any(l))
 
# False, оскільки ітерований об'єкт порожній
l = []
print(any(l))


# Приклад №2: Використання функції any() з рядками в Python
# Всі елементи дорівнюють True
s = "This is good"
print(any(s))
 
# Значення 0 дорівнює False, але тут '0' - це символ рядка, тому він дорівнює True
s = '000'
print(any(s))
 
# False, оскільки ітерований об'єкт порожній
s = ''
print(any(s))










# Функція all() в Python

# Функція all() повертає True, якщо всі елементи заданого ітерованого об’єкта дорівнюють True. Якщо ні, повертається False.

boolean_list = ['True', 'True', 'True']
 
# Перевіряємо, чи всі елементи дорівнюють True
result = all(boolean_list)
print(result)







# Функція ascii() в Python
# Функція ascii() замінює недрукований символ його відповідним ASCII-значенням та повертає його.

text = 'Pythön is interesting'
 
# Замінюємо ö на його ASCII-значення
print(ascii(text))








# Функція bin() в Python
# Функція bin() конвертує вказане ціле число у його двійкове представлення та повертає його.

number = 10
binary = bin(number)
print(binary)



class Quantity:
    apple = 1
    orange = 2
    grapes = 2
    
    def __index__(self):
        return self.apple + self.orange + self.grapes
        
print('The binary equivalent of quantity is:', bin(Quantity()))

# The binary equivalent of quantity is: 0b101

# Тут ми передали об’єкт класу Quantity у функцію bin(). Функція bin() не генерує помилку TypeError, 
# навіть якщо об’єкт Quantity не є цілим числом. Це тому, що ми використали метод __index__(), який повертає ціле число.







# Функція bool() в Python
test = 1
 
# Повертаємо логічне значення змінної test
print(test, 'is', bool(test))


test = 254
# bool() з цілим числом
print(test, 'is', bool(test))
 
test1 = 25.14
# bool() з числом з плаваючою крапкою
print(test1, 'is', bool(test1))
 
test2 = 'Python is the best'
# bool() з рядком
print(test2, 'is', bool(test2))
 
test3 = True
# bool() з True
print(test3, 'is', bool(test3))







# Функція bytearray() в Python
# Функція bytearray() повертає об’єкт bytearray, який є масивом вказаних байтів.


prime_numbers = [2, 3, 5, 7]
 
# Конвертуємо список у bytearray
byte_array = bytearray(prime_numbers)
print(byte_array)


# Приклад №1: Масив байтів із рядка
string = "Python is interesting."
 
# Рядок з кодуванням 'utf-8'
arr = bytearray(string, 'utf-8')
print(arr)



# Приклад №2: Масив байтів вказаного цілочисельного розміру
size = 5
 
arr = bytearray(size)
print(arr)



# Приклад №3: Масив байтів з ітерованого списку

rList = [1, 2, 3, 4, 5]
 
arr = bytearray(rList)
print(arr)








# Функція callable() в Python
# Функція callable() повертає True, якщо вказаний об’єкт викликається, в протилежному випадку повертається False.

# Приклад №1: Як працює функція callable()?
x = 5
print(callable(x))
 
def testFunction():
  print("Test")
 
y = testFunction
print(callable(y))


# Приклад №2: Викликаний об’єкт
class Foo:
  def __call__(self):
    print('Print Something')
 
print(callable(Foo))

# Результат:
# True


# Об’єкт класу Foo може викликатися (і викликається у даному випадку):
class Foo:
  def __call__(self):
    print('Print Something')
 
InstanceOfFoo = Foo()
 
InstanceOfFoo()

# Результат:
# Print Something




# Функція bytes() в Python
# Функція bytes() повертає незмінюваний об’єкт bytes, ініціалізований вказаними даними та розміром.









# Функція chr() в Python
# Функція chr() конвертує ціле число в Unicode-символ і повертає його.

print(chr(97))
 
print(chr(98))

# Результат:
# a
# b

# Приклад №1: Функція chr() із цілими числами в Python


print(chr(97))
print(chr(65))
print(chr(1200))


# Приклад №2: Функція chr() з цілим числом поза допустимим діапазоном
# print(chr(-1000))
# print(chr(1114113))


# Результат:

# ValueError: chr() arg not in range(0x110000)

# Ми вказали цілочисельні аргументи поза допустимим діапазоном: -1000 та 1114113. В результаті отримали помилку ValueError.







# Функція compile() в Python
# Функція compile() обчислює код Python з вихідного об’єкта та повертає його.

codeInString = 'a = 8\nb=7\nsum=a+b\nprint("sum =",sum)'
codeObject = compile(codeInString, 'sumstring', 'exec')
 
exec(codeObject)







# Функція classmethod() в Python
# Функція classmethod() повертає метод класу для вказаної функції.

class Student:
  marks = 0
 
  def compute_marks(self, obtained_marks):
    marks = obtained_marks
    print('Obtained Marks:', marks)
 
# Конвертуємо compute_marks() в метод класу
Student.print_marks = classmethod(Student.compute_marks)
Student.print_marks(88)

# Результат:
# Obtained Marks: 88

# Функція classmethod() приймає один параметр:
# function — функція, яку необхідно перетворити на метод класу.



# Коли слід використовувати метод класу?
# 1. Фабричні методи
# Фабричні методи — це методи, які повертають об’єкт класу (наприклад, конструктор) для різних варіантів використання. 
# Це схоже на перевантаження функцій у С++. Оскільки в Python нічого такого немає, то використовуються методи класу та статичні методи.


from datetime import date
 
# Випадковий Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)
 
    def display(self):
        print(self.name + "'s age is: " + str(self.age))
 
person = Person('Adam', 19)
person.display()
 
person1 = Person.fromBirthYear('John',  1985)
person1.display()


# https://acode.com.ua/function-classmethod-python/








# Функція complex() в Python
# Функція complex() повертає комплексне число, вказуючи дійсну та уявну частини.

# Приклад №1: Як створити комплексне число в Python?

z = complex(2, -3)
print(z)
 
z = complex(1)
print(z)
 
z = complex()
print(z)
 
z = complex('5-9j')
print(z)

# Результат:
# (2-3j)
# (1+0j)
# 0j
# (5-9j)





# Функція delattr() в Python
# Функція delattr() видаляє вказаний атрибут із вказаного об’єкту.


# delattr(object, name)

# Приклад №1: Як працює функція delattr()?

class Coordinate:
  x = 10
  y = -5
  z = 0
 
point1 = Coordinate() 
 
print('x = ',point1.x)
print('y = ',point1.y)
print('z = ',point1.z)
 
delattr(Coordinate, 'z')
 
print('--After deleting z attribute--')
print('x = ',point1.x)
print('y = ',point1.y)
 
# Викличе помилку
print('z = ',point1.z)

# Приклад №2: Видалення атрибута з використанням оператора del
# Ми також можемо видалити атрибут об’єкта за допомогою оператора del.

class Coordinate:
  x = 10
  y = -5
  z = 0


 
point1 = Coordinate() 
 
print('x = ',point1.x)
print('y = ',point1.y)
print('z = ',point1.z)
 
# Видаляємо атрибут z
del Coordinate.z
 
print('--After deleting z attribute--')
print('x = ',point1.x)
print('y = ',point1.y)
 
# Викличе помилку
print('z = ',point1.z)







# Функція dict() в Python
# Функція dict() створює словник у Python. Словник — це невпорядкована, змінювана та індексована колекція.

# Приклад №1: Створення словника лише за допомогою ключових аргументів
numbers = dict(x=5, y=0)
print('numbers =', numbers)
print(type(numbers))
 
empty = dict()
print('empty =', empty)
print(type(empty))


# Ключовий аргумент не передано
numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =',numbers1)
 
# Ключовий аргумент передано
numbers2 = dict([('x', 5), ('y', -5)], z=8)
print('numbers2 =',numbers2)
 
# Функція zip() створює ітерований об'єкт в Python 3
numbers3 = dict(zip(['x', 'y', 'z'], [1, 2, 3]))
print('numbers3 =',numbers3)


# Результат:
# numbers1 = {'y': -5, 'x': 5}
# numbers2 = {'z': 8, 'y': -5, 'x': 5}
# numbers3 = {'z': 3, 'y': 2, 'x': 1}

# Приклад №3: Створення словника за допомогою співставлень

numbers1 = dict({'x': 4, 'y': 5})
print('numbers1 =',numbers1)
 
# Нам не потрібно використовувати dict() у цьому коді
numbers2 = {'x': 4, 'y': 5}
print('numbers2 =',numbers2)
 
# Ключовий аргумент передано
numbers3 = dict({'x': 4, 'y': 5}, z=8)
print('numbers3 =',numbers3)









# Ось оцінка функцій Python за частотою застосування, де 1 — рідко використовуються, а 10 — дуже часто використовуються. Розділю функції на обов'язкові для знання та бажані для знання:

# ### Обов'язкові функції (10-7)
# 1. **print()** - 10
# 2. **len()** - 10
# 3. **str()** - 10
# 4. **int()** - 10
# 5. **float()** - 10
# 6. **input()** - 9
# 7. **range()** - 9
# 8. **list()** - 9
# 9. **dict()** - 9
# 10. **set()** - 8
# 11. **max()** - 8
# 12. **min()** - 8
# 13. **sum()** - 8
# 14. **abs()** - 8
# 15. **enumerate()** - 8
# 16. **zip()** - 7
# 17. **any()** - 7
# 18. **all()** - 7
# 19. **filter()** - 7
# 20. **map()** - 7


# Ця оцінка може змінюватися в залежності від конкретних випадків використання та особистого досвіду, але загалом це базовий підхід для початківців в Python.





# Ось опис обов'язкових функцій у Python з коротким поясненням і прикладом застосування для кожної:

### 1. **print()**
  #  - **Опис:** Виводить дані на екран.
  #  - **Приклад:**

print("Hello, World!")
     

### 2. **len()**
  #  - **Опис:** Повертає довжину (кількість елементів) об'єкта, такого як список, рядок тощо.
  #  - **Приклад:**

     my_list = [1, 2, 3, 4]
     print(len(my_list))  # Виведе: 4
     

### 3. **str()**
  #  - **Опис:** Перетворює об'єкт у рядок.
  #  - **Приклад:**
    #  python
     num = 5
     print(str(num))  # Виведе: '5'
     

### 4. **int()**
  #  - **Опис:** Перетворює об'єкт у ціле число.
  #  - **Приклад:**
    #  python
     float_num = 3.14
     print(int(float_num))  # Виведе: 3
     

### 5. **float()**
  #  - **Опис:** Перетворює об'єкт у число з плаваючою крапкою.
  #  - **Приклад:**

     int_num = 10
     print(float(int_num))  # Виведе: 10.0
     

### 6. **input()**
  #  - **Опис:** Отримує ввід від користувача.
  #  - **Приклад:**
    #  python
     name = input("Enter your name: ")
     print("Hello, " + name)
     

### 7. **range()**
  #  - **Опис:** Створює послідовність чисел, яка часто використовується в циклах.
  #  - **Приклад:**

     for i in range(5):
         print(i)  # Виведе: 0 1 2 3 4
     

### 8. **list()**
  #  - **Опис:** Створює новий список.
  #  - **Приклад:**

     my_list = list((1, 2, 3))
     print(my_list)  # Виведе: [1, 2, 3]
     

### 9. **dict()**
  #  - **Опис:** Створює новий словник.
  # #  - **Приклад:**
    #  python
     my_dict = dict(name="Alice", age=25)
     print(my_dict)  # Виведе: {'name': 'Alice', 'age': 25}
     

### 10. **set()**
  #  - **Опис:** Створює множину, яка є колекцією унікальних елементів.
  #  - **Приклад:**

     my_set = set([1, 2, 2, 3])
     print(my_set)  # Виведе: {1, 2, 3}
     

### 11. **max()**
  #  - **Опис:** Повертає максимальне значення з колекції.
  #  - **Приклад:**

     numbers = [1, 5, 3]
     print(max(numbers))  # Виведе: 5
     

### 12. **min()**
  #  - **Опис:** Повертає мінімальне значення з колекції.
  #  - **Приклад:**

     numbers = [1, 5, 3]
     print(min(numbers))  # Виведе: 1
     

### 13. **sum()**
  #  - **Опис:** Повертає суму всіх елементів у колекції.
  #  - **Приклад:**

     numbers = [1, 2, 3]
     print(sum(numbers))  # Виведе: 6
     

### 14. **abs()**
  #  - **Опис:** Повертає абсолютне значення числа.
  #  - **Приклад:**

     num = -5
     print(abs(num))  # Виведе: 5
     

### 15. **enumerate()**
  #  - **Опис:** Додає лічильник до ітерації, дозволяючи отримувати індекс елемента.
  #  - **Приклад:**
     fruits = ['apple', 'banana', 'cherry']
     for index, fruit in enumerate(fruits):
         print(index, fruit)
     # Виведе:
     # 0 apple
     # 1 banana
     # 2 cherry


### 16. **zip()**
  #  - **Опис:** Об'єднує кілька ітерацій в одну, створюючи пари елементів.
  #  - **Приклад:**

     names = ['Alice', 'Bob', 'Charlie']
     ages = [25, 30, 35]
     for name, age in zip(names, ages):
         print(name, age)
     # Виведе:
     # Alice 25
     # Bob 30
     # Charlie 35
     

### 17. **any()**
  #  - **Опис:** Повертає True, якщо будь-який елемент в ітерації істинний.
  #  - **Приклад:**

     numbers = [0, 0, 1, 0]
     print(any(numbers))  # Виведе: True
     

### 18. **all()**
  #  - **Опис:** Повертає True, якщо всі елементи в ітерації істинні.
  #  - **Приклад:**

     numbers = [1, 2, 3]
     print(all(numbers))  # Виведе: True
     

### 19. **filter()**
  #  - **Опис:** Дозволяє фільтрувати елементи з ітерації на основі умови.
  #  - **Приклад:**

     numbers = [1, 2, 3, 4, 5]
     even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
     print(even_numbers)  # Виведе: [2, 4]
     

### 20. **map()**
  #  - **Опис:** Дозволяє застосувати функцію до кожного елемента ітерації.
  #  - **Приклад:**
  # 
     numbers = [1, 2, 3]
     squared = list(map(lambda x: x ** 2, numbers))
     print(squared)  # Виведе: [1, 4, 9]
     

# Ці функції є базовими для програмування на Python, і їхнє знання допоможе вам у різних завданнях.















# ### Бажані функції (6-1)
# 1. **sorted()** - 6
# 2. **reversed()** - 6
# 3. **hash()** - 6
# 4. **dir()** - 6
# 5. **help()** - 6
# 6. **type()** - 5
# 7. **isinstance()** - 5
# 8. **issubclass()** - 5
# 9. **callable()** - 5
# 10. **slice()** - 5
# 11. **memoryview()** - 4
# 12. **frozenset()** - 4
# 13. **ord()** - 4
# 14. **chr()** - 4
# 15. **oct()** - 3
# 16. **bin()** - 3
# 17. **complex()** - 3
# 18. **divmod()** - 3
# 19. **pow()** - 3
# 20. **round()** - 3
# 21. **format()** - 2
# 22. **globals()** - 2
# 23. **locals()** - 2
# 24. **vars()** - 2
# 25. **delattr()** - 1
# 26. **setattr()** - 1
# 27. **staticmethod()** - 1
# 28. **classmethod()** - 1
# 29. **exec()** - 1
# 30. **eval()** - 1
# 31. **compile()** - 1
# 32. **bytearray()** - 1
# 33. **bytes()** - 1
# 34. **object()** - 1




# Ось короткий опис бажаних функцій із прикладами їх застосування:


### 1. **`sorted()` (6)**
  #  - **Опис**: Сортує ітерабельний об'єкт і повертає новий відсортований список.
  #  - **Приклад**:
   
   fruits = ['banana', 'apple', 'cherry']
   print(sorted(fruits))  # Виведе: ['apple', 'banana', 'cherry']
   

### 2. **`reversed()` (6)**
  #  - **Опис**: Повертає ітератор, що проходить через елементи у зворотному порядку.
  #  - **Приклад**:
   
   numbers = [1, 2, 3]
   print(list(reversed(numbers)))  # Виведе: [3, 2, 1]
   

### 3. **`hash()` (6)**
  #  - **Опис**: Повертає хеш значення об'єкта, який є незмінним (immutable), наприклад, рядка чи кортежу.
  #  - **Приклад**:
   
   print(hash("Hello"))  # Виведе: деяке числове значення
   

### 4. **`dir()` (6)**
  #  - **Опис**: Повертає список атрибутів і методів об'єкта.
  #  - **Приклад**:
   
   class Sample:
       pass
   
   print(dir(Sample))  # Виведе: список атрибутів класу Sample
   

### 5. **`help()` (6)**
  #  - **Опис**: Виводить документацію для об'єкта, функції або модуля.
  #  - **Приклад**:
   
   help(str)  # Виведе документацію для типу str
   

### 6. **`type()` (5)**
  #  - **Опис**: Повертає тип об'єкта.
  #  - **Приклад**:
   
   print(type(42))  # Виведе: <class 'int'>
   

### 7. **`isinstance()` (5)**
  #  - **Опис**: Перевіряє, чи є об'єкт екземпляром зазначеного класу або кортежу класів.
  #  - **Приклад**:
   
   print(isinstance(5, int))  # Виведе: True
   

### 8. **`issubclass()` (5)**
  #  - **Опис**: Перевіряє, чи є клас підкласом іншого класу.
  #  - **Приклад**:
   
   class Animal: pass
   class Dog(Animal): pass

   print(issubclass(Dog, Animal))  # Виведе: True
   

### 9. **`callable()` (5)**
  #  - **Опис**: Перевіряє, чи може об'єкт бути викликаний (як функція).
  #  - **Приклад**:
   
   def func(): pass
   print(callable(func))  # Виведе: True
   

### 10. **`slice()` (5)**
  #  - **Опис**: Створює об'єкт слайсу, який може бути використаний для нарізки списків і інших ітерацій.
  #  - **Приклад**:
   
   my_list = [0, 1, 2, 3, 4]
   s = slice(1, 4)
   print(my_list[s])  # Виведе: [1, 2, 3]
   

### 11. **`memoryview()` (4)**
  #  - **Опис**: Повертає об'єкт, що дозволяє доступ до пам'яті об'єкта без копіювання даних.
  #  - **Приклад**:
   
   data = bytearray(b"Hello")
   mv = memoryview(data)
   print(mv[0])  # Виведе: 72 (ASCII код 'H')
   

### 12. **`frozenset()` (4)**
  #  - **Опис**: Створює незмінний (immutable) набір.
  #  - **Приклад**:
   
   my_set = frozenset([1, 2, 3])
   print(my_set)  # Виведе: frozenset({1, 2, 3})
   

### 13. **`ord()` (4)**
  #  - **Опис**: Повертає числовий код символу.
  #  - **Приклад**:
   
   print(ord('A'))  # Виведе: 65
   

### 14. **`chr()` (4)**
  #  - **Опис**: Повертає символ з відповідним числовим кодом.
  #  - **Приклад**:
   
   print(chr(65))  # Виведе: 'A'
   

### 15. **`oct()` (3)**
  #  - **Опис**: Повертає рядок, що представляє число у восьмеричній системі.
  #  - **Приклад**:
   
   print(oct(8))  # Виведе: '0o10'
   

### 16. **`bin()` (3)**
  #  - **Опис**: Повертає рядок, що представляє число у двійковій системі.
  #  - **Приклад**:
   
   print(bin(4))  # Виведе: '0b100'
   

### 17. **`complex()` (3)**
  #  - **Опис**: Створює комплексне число.
  #  - **Приклад**:
   
   z = complex(1, 2)
   print(z)  # Виведе: (1+2j)
   

### 18. **`divmod()` (3)**
  #  - **Опис**: Повертає кортеж з частки та остачі від ділення.
  #  - **Приклад**:
   
   print(divmod(9, 4))  # Виведе: (2, 1)
   

### 19. **`pow()` (3)**
  #  - **Опис**: Повертає значення числа піднятого до степеня.
  #  - **Приклад**:
   
   print(pow(2, 3))  # Виведе: 8
   

### 20. **`round()` (3)**
  #  - **Опис**: Округлює число до найближчого цілого або до заданої кількості знаків після коми.
  #  - **Приклад**:
   
   print(round(3.14159, 2))  # Виведе: 3.14
   

### 21. **`format()` (2)**
  #  - **Опис**: Форматує значення у рядок згідно з заданим форматом.
  #  - **Приклад**:
   
   print("Hello, {}".format("world"))  # Виведе: Hello, world
   

### 22. **`globals()` (2)**
  #  - **Опис**: Повертає словник глобальних змінних.
  #  - **Приклад**:
   
   a = 10
   print(globals()['a'])  # Виведе: 10
   

### 23. **`locals()` (2)**
  #  - **Опис**: Повертає словник локальних змінних.
  #  - **Приклад**:
   
   def func():
       b = 5
       print(locals()['b'])  # Виведе: 5
   func()
   

### 24. **`vars()` (2)**
  #  - **Опис**: Повертає атрибути об'єкта у вигляді словника.
  #  - **Приклад**:
   
   class Person:
       def __init__(self, name):
           self.name = name
   
   p = Person("Alice")
   print(vars(p))  # Виведе: {'name': 'Alice'}
   

### 25. **`delattr()` (1)**
  #  - **Опис**: Видаляє атрибут з об'єкта.
  #  - **Приклад**:
   
   class Person:
       pass
   
   p = Person()
   p.name = "Alice"
   delattr(p, 'name')
   print(hasattr(p, 'name'))  # Виведе: False
   

### 26. **`setattr()` (1)**
  #  - **Опис**: Встановлює значення атрибуту об'єкта.
  #  - **Приклад**:
   
   class Person:
       pass
   
   p = Person()
   setattr(p, 'name', 'Alice')
   print(p.name)  

# Виведе: Alice



# Функція getattr() в Python використовується для отримання 
# значення атрибута об'єкта за його назвою (як рядок).
# Якщо атрибут не існує, можна вказати значення за замовчуванням, яке буде повернено, щоб уникнути помилки.

class MyClass:
    def __init__(self):
        self.name = "ChatGPT"
        self.age = 3

obj = MyClass()

# Отримуємо значення атрибута 'name'
name = getattr(obj, 'name')
print(name)  # Виведе: ChatGPT

# Отримуємо значення атрибута 'age'
age = getattr(obj, 'age')
print(age)  # Виведе: 3


# Приклад 2: З використанням значення за замовчуванням
# Якщо атрибут не існує, повернемо значення за замовчуванням
height = getattr(obj, 'height', 180)
print(height)  # Виведе: 180, оскільки 'height' немає в obj





# Приклад 3: Виклик методу за допомогою getattr()
class MyClass:
    def greet(self):
        return "Hello!"

obj = MyClass()

# Викликаємо метод 'greet' через getattr
method = getattr(obj, 'greet')
print(method())  # Виведе: Hello!