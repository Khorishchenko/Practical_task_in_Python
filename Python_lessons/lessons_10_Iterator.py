# 1. Ітератори в Python
# Ітератори — це об'єкти, які можуть послідовно перебирати елементи контейнера
# (наприклад, списку або словника). 
# Будь-який об'єкт, який підтримує методи __iter__() і __next__(), може бути ітератором.
# https://acode.com.ua/iterators-python/


# 1. Приклади ��тераторів в Python
my_list = [1, 2, 3]
iterator = iter(my_list)  # Отримуємо ітератор

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3

# Автоматична ітерація
# Елегантніший спосіб виконання автоматичної ітерації — використання циклу for. Наприклад:

# Визначаємо список
my_list = [4, 7, 0]
 
for element in my_list:
    print(element)

# Ітератори та цикл for
# Цикл for в Python використовується для ітерації по послідовності елементів, таких як список, 
# кортеж або рядок. Коли ми використовуємо цикл for з ітератором, 
# цикл автоматично перебиратиме елементи ітератора до тих пір, поки вони не закінчаться. Наприклад: 

# Створюємо список цілих чисел
my_list = [1, 2, 3, 4, 5]
 
# Створюємо ітератор зі списку
iterator = iter(my_list)
 
# Перебираємо елементи ітератора
for element in iterator:
 
    # Виводимо кожен елемент на екран
    print(element)



# Створення користувацьких ітераторів в Python
class PowTwo:
    def __init__(self, max=0):
        self.max = max
 
    def __iter__(self):
        self.n = 0
        return self
 
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
 
 
# Створюємо об'єкт
numbers = PowTwo(3)
 
# Створюємо ітератор з об'єкта
i = iter(numbers)
 
# Використовуємо next для переходу до наступного елемента ітератора
print(next(i)) 
print(next(i)) 
print(next(i)) 
print(next(i)) 
print(next(i)) # генерується виняток StopIteration


# Ми також можемо використовувати цикл for для ітерації по нашому класу:\
for i in PowTwo(3):
    print(i)

    