# 1. Створення та використання функцій
# Напишіть функцію calculate_area, яка обчислює площу прямокутника. Функція повинна приймати два аргументи: довжину та ширину прямокутника, і повертати його площу.

def calculate_area(length, width):
    return length * width

area = calculate_area(width= 10, length= 20)
print("area = ", area)





# 2. Параметри та аргументи функції
# Напишіть функцію greet_user, яка приймає два аргументи: ім'я користувача та привітання. Функція повинна виводити на екран привітання разом з ім'ям користувача.

def greet_user(name, greeting):
    print("hello ", name, greeting)

greet_user("Anton", "Welcome !!!")






# 3. Лямбда-функції
# Напишіть лямбда-функцію multiply, яка приймає два аргументи та повертає їх добуток. Використайте цю лямбда-функцію для обчислення добутку чисел 4 та 5.

multiply = lambda x, y: x * y

# Використання лямбда-функції
result = multiply(4, 5)
print(result)  # Очікуваний результат: 20






# 4. Область видимості змінних

# Напишіть програму, яка має функцію outer_function. 
# Всередині outer_function створіть змінну outer_var і функцію inner_function, яка виводить значення outer_var. 
# Викличте inner_function всередині outer_function.


def outer_function():
    outer_var = "Змінна зовнішньої функції"
    
    def inner_function():
        print(outer_var)

    inner_function()

outer_function()




# 5. Ключове слово global

# Напишіть програму, яка має глобальну змінну counter. Створіть функцію increment_counter, яка збільшує значення counter на 1, 
# використовуючи ключове слово global. Викличте increment_counter декілька разів та виведіть значення counter до та після викликів.

counter = 0

def increment_counter():
    global counter
    counter += 1

print("Початкове значення counter:", counter)
increment_counter()
increment_counter()
increment_counter()
print("Значення counter після викликів:", counter)