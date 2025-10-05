#1
x = int(input("Введите число от 1 до 9: "))

if 1 <= x <= 3:
    s = input("Введите строку: ")
    n = int(input("Введите количество повторов: "))
    for i in range(n):
        print(s)
elif 4 <= x <= 6:
    m = int(input("Введите степень, в которую возвести число: "))
    result = x ** m
    print("Результат возведения в степень:", result)
elif 7 <= x <= 9:
    for i in range(10):
        x += 1
        print(x)
else:
    print("Ошибка ввода")

#2
print("Общество в начале XXI века")

age = int(input("Введите ваш возраст: "))

if 0 <= age < 7:
    print("Вам в детский сад")
elif 7 <= age < 18:
    print("Вам в школу")
elif 18 <= age < 25:
    print("Вам в профессиональное учебное заведение")
elif 25 <= age < 60:
    print("Вам на работу")
elif 60 <= age <= 120:
    print("Вам предоставляется выбор")
else:
    for i in range(5):
        print("Ошибка! Это программа для людей!")