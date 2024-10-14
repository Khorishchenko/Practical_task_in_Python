

# Частина 4: Змінні, Константи та Літерали

value_int = 10
value_char = 'A'
value_double = 10.5

print (f"value int : {value_int} ", type(value_int))
print (f"value char : {value_char} ", type(value_char))
print (f"value double : {value_double} ", type(value_double))


# Константи:
# Створіть константу SIZE та використайте її у програмі.

SIZE = 10
print(f"SIZE : {SIZE}")



# Перетворення типів даних:
# Створіть програму, яка перетворює значення з одного типу даних в інший 
# (наприклад, з int у float, з str у int).

tmp_int = 10

tmp_float = float(tmp_int)
print(tmp_float, type(tmp_float) )

tmp_str = "233"

tmp_int = int(tmp_str)
print (tmp_int, type(tmp_int))


# Напишіть програму, яка запитує у користувача його ім'я та вік, а потім виводить їх на екран.


name = input("яка запитує у користувача його ім'я: ")
age = int(input("яка запитує у користувача його вік:"))

print(f"name is {name}, age is {age}")


# Напишіть програму, яка порівнює два числа та виводить результат порівняння.


value_a = 10
value_b = 15

print ( value_a == value_b )
print (not value_a == value_b )


if value_b == 15 or value_b == 20:
    print(True)
else:
    pass
