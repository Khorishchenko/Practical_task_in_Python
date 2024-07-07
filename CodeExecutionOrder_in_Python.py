# Порядок виконання коду в Python

# Оператори if else в Python
# В Python існує три форми оператора if...else:

#    оператор if

#    оператор if...else

#    оператор if...elif...else

number = 15
 
# Перевіряємо, чи більше 0 значення змінної number
if number > 0:
    print('Number is positive.')
 
print('The if statement is easy')






# Оператор if…else в Python
number = 15
 
if number > 0:
    print('Positive number')
 
else:
    print('Negative number')
 
print('This statement is always executed')





# Оператор if…elif…else в Python
number = 0
 
if number > 0:
    print("Positive number")
 
elif number == 0:
    print('Zero')
else:
    print('Negative number')
 
print('This statement is always executed')






# Вкладені оператори if в Python
number = 10
 
# Зовнішній оператор if
if (number >= 0):
    # Внутрішній оператор if
    if number == 0:
      print('Number is 0')
    
    # Внутрішній оператор else
    else:
        print('Number is positive')
 
# Зовнішній оператор else
else:
    print('Number is negative')










# Цикл for в Python
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





# Використовуємо функцію range() для визначення діапазону значень
values = range(4)
 
# Виконуємо ітерації з i = 0 до i = 3
for i in values:
    print(i)



# Цикл while в Python
