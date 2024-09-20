# Декоратор @property в Python https://acode.com.ua/property-decorator-python/

# Python надає вбудований декоратор @property, який значно спрощує використання геттерів та сеттерів у об’єктно-орієнтованому програмуванні.
# Перш ніж ми розглянемо, що є декоратором @property, давайте спочатку розберемося, навіщо він взагалі потрібен.




# Клас без геттерів та сеттерів
# Припустимо, що ми вирішили створити клас, який зберігає температуру в градусах за Цельсієм, 
# та метод для конвертації температури із градусів за Цельсієм у градуси за Фаренгейтом. Це можна зробити наступним чином:

# Базові методи встановлення та отримання атрибутів в Python
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature
 
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
 
 
# Створюємо новий об'єкт
human = Celsius()
 
# Встановлюємо температуру
human.temperature = 37
 
# Виводимо температуру в градусах за Цельсієм
print(human.temperature)
 
# Виконуємо конвертацію та виводимо температуру в градусах за Фаренгейтом
print(human.to_fahrenheit())





# Використання геттерів та сеттерів
# Припустимо, що ми хочемо розширити можливості використання класу Celsius, визначеного вище. Ми знаємо, 
# що температура будь-якого об’єкта не може бути нижчою від -273.15 градусів за Цельсієм. Оновимо наш код, щоб реалізувати це обмеження.

# Одним із рішень є приховування атрибута temperature (зробимо його приватним) та визначення нових методів (геттера та сеттера) для роботи з ним.

# Примітка: Геттер — це функція, яка повертає значення змінних членів (атрибутів) класу. Сеттер — це функція, 
# яка дозволяє надавати значення змінним-членам (атрибутам) класу.


# Створюємо методи геттера та сеттера
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)
 
    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32
 
    # Метод-геттер
    def get_temperature(self):
        return self._temperature
 
    # Метод-сеттер
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value
 
 
# Створюємо новий об'єкт, викликається метод set_temperature()
human = Celsius(37)
 
# Отримуємо атрибут температури за допомогою геттера
print(human.get_temperature())
 
# Виконуємо конвертацію температури в градуси за Фаренгейтом
print(human.to_fahrenheit())
 
# Реалізація нових обмежень
human.set_temperature(-300)
 
# Виконуємо конвертацію температури в градуси за Фаренгейтом
print(human.to_fahrenheit())






# У цьому оновленні успішно реалізовано нове обмеження. Тепер ми не зможемо встановлювати температуру нижче -273.15 градусів за Цельсієм.

# Примітка: Насправді приватних змінних в Python немає. Просто існують норми, яких необхідно дотримуватися. 
# Сам Python не накладає жодних обмежень.

# Однак більш серйозна проблема, пов’язана з цим оновленням, полягає в тому, що всі програми, 
# які використовують наш клас, повинні змінити свій код з obj.temperature на obj.get_temperature(), 
# а всі вирази типу obj.temperature = val на obj.set_temperature(val).

# Такий рефакторинг може викликати проблеми під час роботи з сотнями тисяч рядків коду. 
# Загалом виходить, що наше оновлення не має зворотної сумісності. Саме тут на допомогу приходить декоратор @property.





# Клас property

# Використання класу property 
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature
 
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
 
    # Метод-геттер
    def get_temperature(self):
        print("Getting value...")
        return self._temperature
 
    # Метод-сеттер
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value
 
    # Створюємо об'єкт класу property
    temperature = property(get_temperature, set_temperature)
 
 
human = Celsius(37)
 
print(human.temperature)
 
print(human.to_fahrenheit())
 
human.temperature = -300







# Декоратор @property
# В Python функція property() є вбудованою функцією, яка створює і повертає об’єкт property. Синтаксис цієї функції наступний:

# property(fget=None, fset=None, fdel=None, doc=None)
# Тут:

#    fget — це функція для отримання значення атрибута;

#    fset — це функція для встановлення значення атрибута;

#    fdel — це функція для видалення атрибута;

#    doc — це рядок (як коментар).

# Як видно з реалізації, ці аргументи функції не є обов’язковими.

# Об’єкт property має три методи: getter(), setter() і deleter(), що дозволяють вказати fget, fset та fdel. Це означає, що наступний рядок:


temperature = property(get_temperature,set_temperature)
# Може бути розбитий на:

# Створюємо порожній property
temperature = property()
 
# Присвоюємо fget
temperature = temperature.getter(get_temperature)
 
# Присвоюємо fset
temperature = temperature.setter(set_temperature)






# Вищенаведена конструкція може бути реалізована у вигляді декораторів. 
# Ми можемо навіть не визначати ідентифікатори get_temperature та set_temperature, оскільки вони не потрібні.

# Для цього ми повторно використовуємо ідентифікатор temperature при визначенні наших функцій геттера та сеттера. 
# Наприклад, реалізація за допомогою декоратора @property:

# Використовуємо декоратор @property
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature
 
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
 
    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature
 
    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value
 
 
# Створюємо об'єкт
human = Celsius(37)
 
print(human.temperature)
 
print(human.to_fahrenheit())
 
coldest_thing = Celsius(-300)