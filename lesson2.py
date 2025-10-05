# longest_by_spaces.py Самое длинное слово в строке (слова разделены пробелами)
line = input("Введите строку (слова через пробел): ").strip()
words = [w for w in line.split() if w]  # split() сам схлопывает множественные пробелы
if not words:
    print("Строка пуста")
else:
    longest = max(words, key=len)
    print("Самое длинное слово:", longest, "| Длина:", len(longest))

# longest_by_semicolon.py Самое длинное слово в строке (слова разделены точкой с запятой)
line = input("Введите строку (слова через ';'): ")
parts = [p.strip() for p in line.split(';')]
words = [p for p in parts if p]  # исключаем пустые
if not words:
    print("Строка пуста")
else:
    longest = max(words, key=len)
    print("Самое длинное слово:", longest, "| Длина:", len(longest))

# shortest_by_custom_delim.py Самое короткое слово по разделителю, который вводит пользователь
line = input("Введите строку: ")
delim = input("Введите символ-разделитель (например, ',', '|', '#', ';', ' '): ")
if not delim:
    print("Разделитель пуст. Повторите запуск программы.")
else:
    parts = [p.strip() for p in line.split(delim)]
    words = [p for p in parts if p]
    if not words:
        print("Не найдено ни одного слова.")
    else:
        shortest = min(words, key=len)
        print("Самое короткое слово:", shortest, "| Длина:", len(shortest))

# find_word_in_line.py Поиск введённого слова в введённой строке (без учёта регистра)
import re

line = input("Введите строку: ")
target = input("Введите слово для поиска: ").strip()

if not target:
    print("Пустой шаблон для поиска.")
else:
    pattern = r'\b' + re.escape(target) + r'\b'
    matches = list(re.finditer(pattern, line, flags=re.IGNORECASE))
    if not matches:
        print("Совпадений не найдено.")
    else:
        positions = [m.start() for m in matches]
        print(f"Найдено вхождений: {len(matches)}")
        print("Позиции (индексы с 0):", positions)

# count_words.py Подсчитать количество слов в предложении
line = input("Введите предложение: ").strip()
# split() по умолчанию разбивает по любым пробельным символам (пробел, таб, перевод строки)
words = [w for w in line.split() if w]
print("Количество слов:", len(words))