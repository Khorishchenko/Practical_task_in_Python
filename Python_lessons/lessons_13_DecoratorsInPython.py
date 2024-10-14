# Декоратор в Python — це шаблон проектування, який дозволяє модифікувати роботу функції, обернувши її в іншу функцію. 
# Зовнішня функція називається декоратором, який приймає як аргумент вихідну функцію та повертає її модифіковану версію.
# https://acode.com.ua/decorators-python/



# Що потрібно знати перед вивченням декораторів в Python?
# Перш ніж ми поговоримо про декоратори, нам необхідно засвоїти кілька важливих понять, пов’язаних з функціями в Python. 
# Також слід пам’ятати, що все в Python є об’єктом, навіть функції є об’єктами.

# Вкладені функції
# Ми можемо розмістити одну функцію всередині іншої — це називається вкладеною функцією. Наприклад:


def outer(x):
    def inner(y):
        return x + y
    return inner
 
add_five = outer(5)
result = add_five(6)
print(result) 








# Передача функції як аргумент
# В Python ми можемо передавати функцію як аргумент іншій функції. 


# Наприклад:
def add(x, y):
    return x + y
 
def calculate(func, x, y):
    return func(x, y)
 
result = calculate(add, 4, 6)
print(result)






# Повернення функції у вигляді значення
# В Python ми також можемо повернути функцію у вигляді значення. 

# Наприклад:

def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello
 
greet = greeting("Atlantis")
print(greet())









# Декоратори в Python
# Декоратор — це функція, яка приймає іншу функцію та повертає її модифіковану версію.


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
 
 
def ordinary():
    print("I am ordinary")

# Ми викликаємо функцію ordinary() звичайним способом, тому отримуємо на виході I am ordinary. 
# Тепер викличемо її за допомогою функції-декоратора:

def make_pretty(func):
    # Визначаємо внутрішню функцію 
    def inner():
        # Додаємо функціонал
        print("I got decorated")
 
        # Викликаємо вихідну функцію
        func()
    # Повертаємо внутрішню функцію
    return inner
 
# Визначаємо звичайну функцію
def ordinary():
    print("I am ordinary")
    
# Створюємо функцію-декоратор
decorated_func = make_pretty(ordinary)
 
# Викликаємо функцію-декоратор
decorated_func()






# Символ @ з декоратором
# Замість того, щоб присвоювати виклик функції змінній, Python пропонує більш елегантний спосіб зробити те саме за допомогою символу @. 
# Наприклад:

def make_pretty(func):
 
    def inner():
        print("I got decorated")
        func()
    return inner
 
@make_pretty
def ordinary():
    print("I am ordinary")
 
ordinary()







# Декоратори та Функції з параметрами
# Вищенаведений декоратор простий і працює тільки з функціями, що не мають параметрів. 
# А якби у нас були функції, що приймають параметри, наприклад:

def divide(a, b):
    return a/b


# Ця функція має два параметри: a та b. Ми знаємо, що вона видасть помилку, якщо ми вкажемо в якості аргументу (b) значення 0.

# Тепер зробимо декоратор для перевірки випадку, який може призвести до помилки (ділення на 0):

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return
 
        return func(a, b)
    return inner
 
@smart_divide
def divide(a, b):
    print(a/b)
 
divide(2,5)
 
divide(2,0)






# Ланцюжок декораторів в Python
# В Python можна поєднувати кілька декораторів у ланцюжок.
# Для створення ланцюжка декораторів ми можемо застосувати декілька декораторів до однієї функції, розміщуючи їх один за одним.

def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner
 
 
def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner
 
 
@star
@percent
def printer(msg):
    print(msg)
 
printer("Hello")



# Наступна частина коду:

# @star
# @percent
# def printer(msg):
#     print(msg)
# рівнозначна

# def printer(msg):
#     print(msg)
# printer = star(percent(printer))