# Генератор в Python — це функція, що повертає ітератор, який під час ітерації генерує послідовність значень. 
# Генератори корисні, коли нам потрібно отримати велику послідовність значень, але ми не хочемо зберігати їх всі в пам’яті відразу.

# Як і зі звичайними функціями, функцію-генератор в Python можна визначити за допомогою ключового слова def, але замість оператора return використовується оператор yield.
# def generator_name(arg):
#     # Тіло генератора
#     yield something


# Ось приклад функції-генератора, що генерує послідовність чисел:
def my_generator(n):
 
    # Ініціалізуємо лічильник
    value = 0
 
    # Цикл виконується доти, доки лічильник не стане менше n
    while value < n:
 
        # Повертаємо поточне значення лічильника
        yield value
 
        # Збільшуємо лічильник
        value += 1
 
# Виконуємо ітерацію генератора
for value in my_generator(3):
 
    # Виводимо кожне значення, отримане від генератора
    print(value)


# Генераторні вирази в Python
# Генераторний вираз в Python має наступний синтаксис:
# (вираз for елемент in ітератор)


# Створюємо об'єкт генератора
squares_generator = (i * i for i in range(5))
 
# Ітерація по генератору та вивід значень на екран
for i in squares_generator:
    print(i)




# Користь від генераторів в Python
# Є декілька причин, чому генератори є корисною конструкцією в Python.

# 1. Простота реалізації.
# Генератори створювати простіше, ніж ітератори.

# Ось приклад програми піднесення значень до квадрата на кожній ітерації, використовуючи клас ітератора:

class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max
 
    def __iter__(self):
        return self
 
    def __next__(self):
        if self.n > self.max:
            raise StopIteration
 
        result = 2 ** self.n
        self.n += 1
        return result
    

# А тепер те саме завдання, але з використанням генератора:
def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1


# 2. Ефективність використання пам’яті.
# Звичайна функція, що повертає послідовність, створює всю послідовність у пам’яті, перш ніж повернути результат. Це проблема, коли кількість елементів у 
# послідовності величезна.

# Використання генераторів у подібних випадках не вимагає використання великої кількості пам’яті та є кращим варіантом, оскільки віддає лише один елемент за раз.


# 3. Представлення нескінченного потоку даних.
# Генератори є хорошим засобом для представлення нескінченного потоку даних. Нескінченні потоки неможливо зберігати в пам’яті, 
# а оскільки генератори віддають лише один елемент за раз, вони можуть представляти нескінченний потік даних.

# Наступна функція-генератор може генерувати всі парні числа (принаймні теоретично):

def even_numbers(max=10):
    n = 0
    while n < max:
        yield n
        n += 2



# 4. Обробка кількох операцій.
# Декілька генераторів можна використовувати для обробки відразу кількох операцій. Найкраще це проілюструвати на прикладі.

# Припустимо, у нас є генератор, який генерує послідовність чисел Фібоначчі. Та є ще один генератор для піднесення чисел до квадрата.

# Якщо ми хочемо дізнатися суму квадратів чисел Фібоначчі, ми можемо зробити це, поєднавши разом вихідні дані генераторів:

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x
 
def square(nums):
    for num in nums:
        yield num**2
 
print(sum(square(fibonacci_numbers(10))))








# Генератори в Python мають декілька важливих відмінностей від звичайних функцій:

# ### 1. **Оператор `yield` замість `return`**:
#    - Звичайна функція використовує `return`, щоб повернути значення та завершити виконання.
#    - Генератор використовує `yield`, щоб повернути значення, але **не завершувати** виконання. 
#       Він зберігає свій стан і може продовжити виконання з того місця, де був зупинений, при наступному виклику.

#    **Приклад звичайної функції:**
#    ```python
def normal_function():
       return 1
#    ```

#    **Приклад генератора:**
#    ```python
def generator_function():
       yield 1
#    ```

#    У звичайній функції після `return` виконання функції завершиться, а в генераторі після `yield` можна буде викликати наступний елемент з допомогою функції `next()`.

# ### 2. **Лінива оцінка (Lazy Evaluation)**:
#    - Генератори повертають значення **по одному** за запитом (під час кожного виклику `next()`), замість того, 
#       щоб одразу обчислювати всі значення та зберігати їх у пам'яті, як це роблять звичайні функції, які повертають список чи інші структури даних.
#    - Це особливо корисно для роботи з великими наборами даних, де не потрібно завантажувати все одразу в пам'ять.

#    **Приклад**:
#    ```python
def number_generator():
    for i in range(1000):
        yield i
#    ```

#    Генератор буде по черзі повертати числа від 0 до 999 лише при запиті.

# ### 3. **Стан генератора зберігається між викликами**:
#    - У генераторі при кожному виклику зберігається поточний стан виконання, включно зі змінними, лічильниками та вказівниками на те, де було зупинено виконання.
#    - Це дозволяє генератору **працювати як ітератор**.

#    **Приклад**:
#    ```python
gen = number_generator()
print(next(gen))  # Виведе 0
print(next(gen))  # Виведе 1
#    ```

#    Генератор зберігає своє положення між викликами.

# ### 4. **Необмежені послідовності**:
#    - Генератори можуть генерувати нескінченні послідовності, оскільки вони повертають значення лише за запитом. 
#       У звичайних функціях це неможливо, оскільки вони повертають всі результати одразу.

#    **Приклад нескінченного генератора**:
#    ```python
def infinite_counter():
       i = 0
       while True:
           yield i
           i += 1
#    ```

# ### Висновок:
# - **Звичайні функції**: повертають значення одразу і завершують виконання.
# - **Генератори**: повертають значення по черзі, зберігають свій стан між викликами та використовують менше пам'яті.