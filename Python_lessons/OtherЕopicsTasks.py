# Ітератори в Python

# Генератори в Python

# Замикання в Python

# Декоратори в Python

# Декоратор @property в Python

# Регулярні вирази в Python



# 1. Ітератори в Python
# Завдання: Створіть власний ітератор, який повертатиме тільки парні числа з переданого списку.

class EvenIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.numbers):
            current_number = self.numbers[self.index]
            self.index += 1
            if current_number % 2 == 0:
                return current_number
        raise StopIteration

student_id = [112, 114, 116, 118, 115]  # Используем список вместо множества
even_iterator = EvenIterator(student_id)
for num in even_iterator:
    print(num)
        

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_tuple = (1, 2, 3)

even_iterator = EvenIterator(numbers)
for num in even_iterator:
    print(num)

even_iterator = EvenIterator(my_tuple)
for num in even_iterator:
    print(num)





# 2. Генератори в Python
# Завдання: Напишіть генератор, який повертатиме числа Фібоначчі до заданого значення.

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


fibonacci_generator = fibonacci(100)

for num in fibonacci_generator:
    print(num)





# 3. Замикання в Python
# Завдання: Створіть замикання, яке повертатиме функцію, що додаватиме задане значення до числа.

def adder(number):
    def add(number2):
        return number + number2
    return add

add_five = adder(5)

print(add_five(10))  # Output: 15







# 4. Декоратори в Python
# Завдання: Створіть декоратор, який перед виконанням функції друкуватиме "Виконується функція".

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Виконується функція")
        return func(*args, **kwargs)
    return wrapper

@decorator
def greet(name):
    print(f"Привіт, {name}!")

# Виклик функції
greet("Сергій")




# Ваша пропозиція про те, щоб просто вивести повідомлення "Виконується функція" без використання вкладеної функції, не зовсім коректна. 
# Давайте розглянемо, чому ми використовуємо вкладену функцію (в даному випадку  `wrapper` ) у декораторі.

# ### Основні причини використання вкладеної функції в декораторі:

# 1. **Збереження контексту**:
#    - Вкладена функція  `wrapper`  дозволяє нам зберігати контекст, зокрема, доступ до аргументів, які передаються в декоровану функцію.
# Якщо ви просто виконаєте  `print("Виконується функція")` 
# на рівні декоратора, ви не зможете отримати доступ до аргументів, які передаються в декоровану функцію.

# 2. **Перехоплення виклику функції**:
#    - Декоратор повинен перехоплювати виклик функції, щоб виконати певні дії (наприклад, вивести повідомлення, змінити аргументи,
#     обробити результати). Вкладена функція  `wrapper`  реалізує цю логіку, дозволяючи виконати код перед і після виклику оригінальної функції.

# 3. **Гнучкість**:
#    - Використання вкладеної функції дозволяє декоратору бути більш гнучким. Ви можете додати додаткову логіку до  `wrapper` , 
# таку як обробка винятків, вимірювання часу виконання функції, або навіть модифікація результату, який повертає декорована функція.

# ### Приклад без вкладеної функції:
# Якщо ви спробуєте реалізувати декоратор без вкладеної функції, ваш код не зможе правильно обробити виклики функції:
def decorator(func):
    print("Виконується функція")  # Це виконається лише один раз, коли декоратор визначається
    return func  # Це поверне оригінальну функцію без можливості її модифікації

@decorator
def greet(name):
    print(f"Привіт, {name}!")

# greet("Сергій")
# В цьому випадку повідомлення "Виконується функція" буде надруковано лише один раз під час визначення декоратора, 
# а не кожного разу, коли викликається  `greet` . Таким чином, ми не зможемо перехопити виклики до функції.

# ### Висновок:
# Використання вкладеної функції в декораторі є необхідним для того, щоб правильно обробляти виклики функцій, 
# передавати аргументи і виконувати додаткову логіку перед або після виклику оригінальної функції. 
# Це дозволяє створювати більш складні і гнучкі декоратори.







# 5. Декоратор @property в Python
# Завдання: Створіть клас з властивістю temperature, яка буде повертати значення в градусах Фаренгейта і Цельсія.

class Temp():
    def __init__(self, fahrenheit):
        self._fahrenheit = fahrenheit

    @property
    def celsius(self):
        return (self._fahrenheit - 32) * 5/9
    

temp = Temp(100)

print(temp.celsius)  # Output: 37.77777777777778










# 6. Регулярні вирази в Python
# Завдання: Напишіть функцію, яка перевірятиме, чи є переданий рядок правильною email-адресою.

import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


# Приклад використання
email = "test@example.com"
print(is_valid_email(email))  # Очікуваний результат: True або False

print(validate_email("test@example.com"))  # Output: True




def check_password(password):
    if len(password) < 8:
        return False
    
    has_digit = False
    has_upper = False

    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True

    return has_digit and has_upper

# Приклади використання
print(check_password("Pass1234"))  # True
print(check_password("password"))  # False
print(check_password("12345678"))  # False
print(check_password("P@ssw0rd"))  # True
