# Регулярні вирази в Python
# https://acode.com.ua/regex-python/

# Регулярні вирази в Python (скор. “RegEx” від англ. “Regular Expression”) — це послідовність символів, які визначають шаблон для пошуку відповідностей. Наприклад:

# Python має модуль re для роботи з регулярними виразами. Наприклад:

import re
 
pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)
 
if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")



# Тут ми використали метод re.matches() для пошуку відповідностей шаблону регулярного виразу pattern у рядку test_string. 
# Метод повертає відповідний об’єкт, якщо пошук успішний. Якщо ні, повертається None.





# Використання регулярних виразів у Python
# Python має модуль re для роботи з регулярними виразами. Для їх використання нам потрібно спочатку імпортувати модуль:

import re
# Модуль визначає кілька методів та констант для роботи з регулярними виразами.

# Метод re.findall()
# Метод re.findall() повертає список рядків, які відповідають шаблону регулярного виразу. 
# 
# 
# Наприклад:

# Програма для вилучення чисел з рядка
 
import re
 
string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'
 
result = re.findall(pattern, string) 
print(result)