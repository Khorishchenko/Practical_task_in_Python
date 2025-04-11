# Отримання рядка з консолі

# from colorama import init, Fore, Back, Style

# # Ініціалізуємо colorama
# init()

# # Виводимо текст різними кольорами
# print(Fore.RED + 'Цей текст червоний')
# print(Fore.GREEN + 'Цей текст зелений')
# print(Fore.BLUE + 'Цей текст синій')

# # Виводимо текст з фоном
# print(Back.YELLOW + 'Цей текст на жовтому фоні')

# # Відновлюємо стиль
# print(Style.RESET_ALL + 'Цей текст звичайний')


name = input("Введіть своє ім'я: ")
print(f"Привіт, {name}!")



# Отримання цілого числа з консолі
age = int(input("Введіть свій вік: "))
print(f"Ви ввели вік: {age}")


# Отримання числа з плаваючою комою
height = float(input("Введіть свій зріст у метрах: "))
print(f"Ваш зріст: {height} м")



# Отримання кількох значень одночасно
numbers = input("Введіть три числа, розділених пробілами: ").split()
num1, num2, num3 = map(int, numbers)
print(f"Ви ввели числа: {num1}, {num2}, {num3}")




# Рядок
user_input = input("Введіть рядок: ")
print(f"Ви ввели: {user_input}")

# Ціле число
number = int(input("Введіть ціле число: "))
print(f"Ви ввели ціле число: {number}")

# Число з плаваючою комою
floating_number = float(input("Введіть число з плаваючою комою: "))
print(f"Ви ввели число з плаваючою комою: {floating_number}")