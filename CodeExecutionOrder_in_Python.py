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
# Розглянемо приклад використання циклу while в Python:

# У цій програмі ми виводимо числа від 1 до 5
 
# Ініціалізація змінних
i = 1
n = 5
 
# Цикл while з i = 1 до 5
while i <= n:
    print(i)
    i = i + 1



# У цій програмі ми обчислюємо суму чисел доти,
# доки користувач не введе 0
 
total = 0
 
number = int(input('Enter a number: '))
 
# Додаємо числа, доки number не дорівнюватиме 0
while number != 0:
    total += number  # total = total + number
    
    # Запитуємо користувацький ввід
    number = int(input('Enter a number: '))
    
 
print('total =', total)


# Цикл while з частиною else в Python
# У Python цикл while може мати необов’язковий блок else, який виконуватиметься після того, як умова циклу стане False

counter = 0
 
while counter < 3:
    print('Inside loop')
    counter += 1
else:
    print('Inside else')


# Блок else не виконуватиметься, якщо цикл while зупинено оператором break. Наприклад:
counter = 0
 
while counter < 3:
    # Цикл завершує своє виконання через оператор break.
    # Блок else не виконується 
    if counter == 1:
        break
 
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')



# for проти while в Python
# Цикл for зазвичай використовується, коли відома кількість ітерацій. Наприклад:

# Даний цикл повторюється 4 рази (від 0 до 3)
for i in range(4):
    print(i)

# Цикл while зазвичай використовується, коли кількість ітерацій невідома. Наприклад:

true = 5

while true != 0:
    pass
# Код виконується доти, доки умова не стане False






# Оператори break та continue в Python
# Оператор break в Python



# Оператор pass в Python
# Оператор pass — це порожній оператор, який можна використовувати як “заглушку” для майбутнього коду. 
# Припустимо, ми маємо цикл або функцію, яка ще не визначена, але ми її визначимо в майбутньому. 
# У таких випадках ми можемо використовувати оператор pass.

n = 10
 
# Використовуємо pass всередині конструкції if
if n > 10:
    pass

print('Hello')



# n = 10
 
# if n > 10:
#     # Тут буде код, але трохи пізніше
 
# print('Hello')


# Також ми можемо використати оператор pass у функції чи класі. Наприклад, у функції:

def function(args):
    pass

class Example:
    pass