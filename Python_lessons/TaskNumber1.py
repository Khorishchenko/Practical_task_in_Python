# 1

# sentence = "Python це потужна мова, але Python простий."
# words = sentence.replace(",", "").replace(".", "").split()
# print(words)
# ['Python', 'це', 'потужна', 'мова', 'але', 'Python', 'простий']



text = "Це приклад тексту, в якому є кілька слів. Деякі слова повторюються, слова слова слова"
# Видаляємо розділові знаки та розбиваємо рядок на слова
words = text.lower().replace(",", "").replace(".", "").split()

# Підраховуємо кількість повторень слів
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# print(word_counts)

# # Виводимо результати
# print("Кількість слів:", len(words))

frequent_words = []

# # .items() повертає пари (ключ, значення) у вигляді ітератора, де:

# # ключ — це слово
# значення — це кількість його повторень
for word, count in word_counts.items():
    if count > 3:
        frequent_words.append(word)

# print("Повторювані слова:")
for word in frequent_words:
    print(f"{word}")

print(frequent_words)





#================================================================
# # 2


# Ініціалізація словника продуктів
products = {
    "яблука": 10,
    "банани": 3,
    "молоко": 7,
    "хліб": 2
}

# Функція для оновлення кількості продуктів
def update_product(name, quantity):
    if name in products:
        products[name] += quantity
        if products[name] <= 0:
            del products[name]  # Видалення продукту, якщо кількість 0 або менше
    else:
        if quantity > 0:
            products[name] = quantity  # Додаємо новий продукт

# Оновлення даних
update_product("банани", 2)  
update_product("хліб", -2)  
update_product("яйця", 4)    

# Створення списку продуктів, в яких кількість менше 5
low_stock = []  
for name, qty in products.items():  
    if qty < 5:  
        low_stock.append(name)  


# Вивід результатів
print("Оновлений список продуктів:", products)
print("Продукти з кількістю менше 5:", low_stock)




# #================================================================
# # 3


# # Список продажів
sales = [
    {"продукт": "Яблука", "кількість": 50, "ціна": 20},
    {"продукт": "Банани", "кількість": 30, "ціна": 25},
    {"продукт": "Апельсини", "кількість": 100, "ціна": 15},
    {"продукт": "Груші", "кількість": 40, "ціна": 30},
]

# Функція для обчислення загального доходу
def calculate_revenue(sales_list):
    revenue = {}
    for sale in sales_list:
        product = sale["продукт"]
        total = sale["кількість"] * sale["ціна"]

        if product in revenue:
            revenue[product] += total
        else:
            revenue[product] = total
    return revenue

# Обчислення доходу
revenues = calculate_revenue(sales)

# Список продуктів із доходом більше ніж 1000
high_revenue_products = []
for product, total in revenues.items():
    if total > 1000:
        high_revenue_products.append(product)


# Вивід результатів
print("Загальний дохід по продуктах:", revenues)
print("Продукти, що принесли більше 1000:", high_revenue_products)




#================================================================
# # 4












#================================================================
# # 5


import hashlib

# Створюємо словник користувачів (логін -> {пароль, ПІБ})
users = {
    "user1": {"password": hashlib.md5("password123".encode()).hexdigest(), "full_name": "Sergii Kh"},
    "user2": {"password": hashlib.md5("qwerty".encode()).hexdigest(), "full_name": "Petro Ivanov"},
}

# Функція для перевірки пароля
def check_password(login, password):
    if login in users:
        hashed_input = hashlib.md5(password.encode()).hexdigest()
        if users[login]["password"] == hashed_input:
            return True
    return False

# Введення логіна і пароля
login = input("Введіть логін: ")
password = input("Введіть пароль: ")

# Перевірка
if check_password(login, password):
    print(f"Доступ дозволено, {users[login]['full_name']}!")
else:
    print("Доступ заборонено")
    print("Невірний логін або пароль!")