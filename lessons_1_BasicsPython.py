# Отримання рядка з консолі

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