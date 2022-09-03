# ПЕРЕМЕННЫЕ
# Типы данных справедливы int, float, boolean, strlist и др.
# Python – язык с динамической типизацией
## value = 2809
# name = ‘Elena’

# print('hello world')

# ТИПЫ ДАННЫХ И ПЕРЕМЕННАЯ
## int, float, boolean, str, list, None

# value = None
# print(type(value))
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334
# print(type(value))


# Ввод и вывод данных
# print() – отвечает за вывод данных
# input() – отвечает за ввод данных
# чтобы объявить строку, указываем идентификатор строки (s =) и 'hello world'(значание строки с одинарными кавычками).

# s = 'hello world'
# print(s) # вывод строки

# s = "hello 'world"
# print(s) # вывод строки с одинарной кавычкой

# s = 'hello "world'
# print(s) # вывод строки с двойной кавычкой

# s = 'hello \'world'
# print(s)

# s = 'hello \n world'
# print(s) # вывод строки с переходом на новую строку

# Интерполция. Как вывести значения несколько переменных с оператором - print
# можно сделать указание через запятую
# print(a, b, s)
# print(a, '-',b, '-',  s)
# print('{} - {} - {}'.format(a, b, s)) # формат
# print('{1} - {2} - {0}'.format(a, b, s)) # формат. Здесь можно менять местами значения переменных.
# print(f'{a} - {b} - {s}') # интерполция

# Логическая переменная -  переменная (f) = присвоить значение (True)
# f = True
# print(f)

# Логическая переменная - или переменная (f) = присвоить значение (False)
# f = False
# print(f)

# Списки, заменяющие массивы.
# Простое применение.
# 1
# list = [1, 2, 3]
# 2
# list = ['1', '2', '3']
# col= ['hello', 1, 2, 4.5, True ]
# print(list)
# print(col)

# ВВОД И ВЫВОД ДАННЫХ. ПРЕОБРАЗОВАНИЕ ТИПОВ.
## print, input

# 1 если работаем со строками, то ответ будет 10+20=1020
# print('Введите a');
# a = input()
# print('Введите b');
# b = input()
# print(a, '+',  b, '=', a+b)

# 2 если работаем с целым числом, то  (int ) и ответ будет 10+20=30
# print('Введите a');
# a = int(input())
# print('Введите b');
# b = int(input())
# print(a, '+',  b, '=', a+b)

# 3 если работаем с вещественными числами, то  (float) и ответ будет 1.2+3.4=4.6
# print('Введите a');
# a = float(input())
# print('Введите b');
# b = float(input())
# print(a, '+',  b, '=', a+b)

# print(a, b)
# print('{} {}'.format(a,b))
# print(f'{a} {b}')

# АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ.
# +,-,*,/,%,//,**
# Приоритет операций
# **,⊕,⊖,*,/,//,%,+,-
# ( ) Скобки меняют приоритет

# 1 будет = 444
# a = 123
# b = 321
# c = a + b
# print(c)

# 2 будет = -198
# a = 123
# b = -321
# c = a + b
# print(c)

# ФУНКЦИЯ round
# a = 1.31231223
# b = 3
# c = round(a * b, 7)  # 7 - это семь цыфр после точки, вещественное число.
# print(c)

# СОКРАЩЁННЫЕ ОПЕРАЦИИ ПРИСВАИВАНИЯ.
# 1 результат = 8
# a = 3
# a = a + 5  # или написать так: a += 5
# print(a)

# ЛОГИЧЕСКИЕ ОПЕРАЦИИ.
# >,>=,<,<=,==,!=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in
# gen

# a = 1 > 4 # в терминале будет (False - ложь)
# a = 1 < 4 # в терминале будет (True - истина)
# a = 1 == 2 # Операции сравнения
# a = 1 != 2 # Операция неравенства
# print(a)

# Управляющие конструкции: if, if-else
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#    print(a)
# else:
#    print(b )

# Управляющие конструкции: if, if-else
# if condition1:
# operator
# elif condition2:
# operator
# elif condition3:
# operator
# else:
# operator

## username = input('Введите имя: ')
# if username == 'Елена':
##     print('Ура, это же Елена!')
# elif username == 'Ирина':
##     print('Я так ждала Вас, Ирина!')
# elif username == 'Ильнар':
##     print('Ильнар - топ)')
# else:
##     print('Привет, ', username)

# Управляющие конструкции: while - это цикл.
# Цикл позволяет выполнить блок операторов какое- то количество раз
# while condition:
# operator 1
# operator 2
# .. .
# operator n

# original = 23
# inverted = 0
# while original != 0:
#    inverted = inverted * 10 + (original % 10)
#    original //= 10
# print(inverted)

# У ЦИКЛА while ЕСТЬ БЛОК else:
# while condition:
# operator 1
# operator 2
# .. .
# operator n
# else:
# operator n + 1
# operator n + 2
# .. .
# operator n + m

# original = 23
# inverted = 0
# while original != 0:
#    inverted = inverted * 10 + (original % 10)
#    original //= 10
# else:
#    print('Пожалуй')
#    print('хватит )')
# print(inverted)
# Пожалуй
# хватит )
# 32

# Управляющие конструкции: for
# Когда мы знаем, что хотим
# for i in enumeration:
#    # operator 1
# operator 2 #.. .
# operator n

# for i in 1, -2, 3, 14, 5:
#     print(i)
# 1 # -2 #3 # 14 #5

# Знакомьтесь – range
# r = range(5)           # range(0, 5)
# r = range(2, 5)        # range(2, 5)
# r = range(-5, 0)       # range(-5, 0)
# r = range(1, 10, 2)    # range(1, 10, 2)
# r = range(100, 0, -20) # range(100, 0, -20)

## Немного о строках
# text = 'съешь ещё этих мягких французских булок'
# print(len(text))
# print('ещё' in text) print(text.isdigit()) print(text.islower()) print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#    print(c)


## Немного о строках
text = 'съешь ещё этих мягких французских булок'
print(text[0])   # c
print(text[1])   # ъ
print(text[len(text)-1])  # к
print(text[-5])  # б
print(text[:])   # print(text)
print(text[:2])  # съ
print(text[len(text)-2:])  # ок
print(text[2:9])  # ешь ещё
print(text[6:-18])  # ещё этих мягких
print(text[0:len(text):6])  # сеикакл
print(text[::6])  # сеикакл
text = text[2:9] + text[-5] + text[:2]  # ...
