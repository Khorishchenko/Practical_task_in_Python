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




# Використання циклу for
for i in range(10):
    print(f"Ітерація {i + 1}")

# Використання циклу while
i = 0
while i < 10:
    print(f"Ітерація {i + 1}")
    i += 1




# Використання else
for i in range(10):
    print(i)
else:
    print("Цикл завершено")





# Цикл for з списком
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)




# Цикл for з рядком
word = "hello"
for char in word:
    print(char)
