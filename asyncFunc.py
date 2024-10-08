# У Python async та await — це ключові слова, які використовуються для написання асинхронних функцій. 
# Вони дозволяють створювати код, який не блокує виконання програми під час виконання довготривалих операцій, 
# таких як запити до API, робота з базою даних, введення/виведення або затримки.

# Як працюють async та await?
# async — використовується для оголошення асинхронної функції. Це функція, яка працює асинхронно, 
# тобто вона може бути зупинена під час виконання для очікування інших операцій без блокування основного потоку програми.

# await — використовується всередині асинхронних функцій для того, щоб "чекати" результату іншої асинхронної операції або функції. 
# Виклик await тимчасово призупиняє виконання поточної функції, дозволяючи іншим задачам виконуватися паралельно.

# Асинхронна функція
# Ось як створюється асинхронна функція за допомогою async:

async def example_function():
    print("Асинхронна функція почала виконання")
    await some_async_task()  # Чекаємо завершення асинхронної операції
    print("Асинхронна функція завершила виконання")


# Асинхронне очікування
# Функція await використовується для очікування завершення іншої асинхронної функції або корутини:

async def some_async_task():
    await asyncio.sleep(2)  # Чекаємо 2 секунди без блокування
    print("Асинхронна операція завершена")




# Приклад
# Розглянемо приклад, де дві функції виконуються асинхронно і не блокують одна одну:
import asyncio

async def task1():
    print("Задача 1 почалася")
    await asyncio.sleep(2)  # Асинхронна пауза на 2 секунди
    print("Задача 1 завершена")

async def task2():
    print("Задача 2 почалася")
    await asyncio.sleep(1)  # Асинхронна пауза на 1 секунду
    print("Задача 2 завершена")

async def main():
    await asyncio.gather(task1(), task2())  # Виконуємо задачі одночасно

# Запускаємо головну функцію
asyncio.run(main())



# Пояснення:
# async def main() — головна асинхронна функція, яка викликає інші асинхронні задачі.
# await asyncio.gather(task1(), task2()) — одночасно запускає обидві асинхронні функції task1 і task2.
# Використання await asyncio.sleep(2) означає, що задача зупиняється на 2 секунди, але інші задачі можуть виконуватися в цей час.
# Важливі моменти:
# Асинхронний код не блокує основний потік програми, дозволяючи іншим операціям виконуватися паралельно під час очікування.
# Асинхронні функції повинні бути викликані всередині іншої асинхронної функції або керуватися подіями (наприклад, через asyncio.run()).
# Асинхронність у Python використовується для підвищення продуктивності при роботі з мережею, файлами або іншими ресурсами, де операції можуть займати багато часу.