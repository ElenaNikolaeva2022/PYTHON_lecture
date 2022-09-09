# Урок 2. Данные, функции и модули в Python

#  ФАЙЛЫ
# Как работать с файлами:
# Связать файловую переменную с файлом, определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+

# with open('file.txt', 'a') as data:
#     data.write('line 1111\n')
#     data.write('line 2222\n')

# colors = ['red', 'green', 'blue123']
# data = open('file.txt', 'a')
# # data.writelines(colors)                # разделителей не будет
# data.write('LINE 121\n')
# data.write('LINE 131\n')
# data.close()


# exit()                     # позволяет не выполнять код, который ниже в скрипте прописан.
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


# # ФУНКЦИИ И МОДУЛИ
# # Это фрагмент программы, используемый многократно

# # def function_name(x):
# # body line 1
# # .. .
# # body line n
# # optional return

# import leс as l
# print(l.f(1))


# def f(x):
#     return x**2


# # def f(x):                    print(f(1))             # Целое
# #     if x == 1:               print(f(2.3))           # 23
# #         return 'Целое'       print(f(28))            # None
# #     elif x == 2.3:           print(type(f(1)))       # str
# #         return 23            print(type(f(2.3)))     # int
# #     else:                    print(type(f(28)))      # N
# #         return

# # new file function_file.py file hello.py

# # def f(x):                    import function_file
# #     if x == 1:
# #         return 'Целое'
# #     elif x == 2.3:           print(function_file.f(1))       # Целое
# #         return 23            print(function_file.f(2.3))     # 23
# #     else:                    print(function_file.f(28))      # None
# #         return

# # new file function_file.py file hello.py

# # def f(x):                    import function_file as ff
# #     if x == 1:
# #         return 'Целое'
# #     elif x == 2.3:           print(ff.f(1))       # Целое
# #         return 23            print(ff.f(2.3))     # 23
# #     else:                    print(ff.f(28))      # None
# #         return


# # def new_string(symbol, count):
# #     return symbol * count

# # print(new_string('!', 5))           # !!!!!
# # print(new_string('!'))              # TypeError missing 1 required ...


# # def new_string(symbol, count = 3):
# #      return symbol * count
# # print(new_string('!', 5))           # !!!!!
# # print(new_string('!'))              # !!!
# # print(new_string(4))                # 12


# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))  # asdw
# print(concatenatio('a', '1', 'd', '2'))  # a1d2


# def concatenatio(*params):
#     res = 0           # res: int = 0 указания типа int необязательно
#     for item in params:
#         res += item
#     return res
# print(concatenatio(1, 2, 3, 4)) # TypeError: ...


# # РЕКУРСИЯ
# # Функции

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34


# # КОРТЕЖИ (англ. # tuple )
# # Кортеж – это неизменяемый “список”

# t = ()
# print(type(t))          # tuple
# t = (1,)
# print(type(t))          # tuple
# t = (1)
# print(type(t))          # int
# t = (28, 9, 1990)
# print(type(t))          # tuple
# colors = ['red', 'green', 'blue']
# print(colors)            # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t)                 # ('red', 'green', 'blue')

# # Пример:
# # a, b = 3, 4     # обычное множественное присваивание к a цифру 3, к b цифру 4
# (a) = (3, 4) # обрамление скобками, то получится КОРТЕЖ
# print(a)
# print(a[0])
# # в Терминале будет:
# # (3, 4)
# # 3


# (a) = (3, 1, 41, 4)
# print(a)
# print(a[-2])
# # если укажем [-2], то в Терминале будет:
# # (3, 1, 41, 4)
# # 41

# (a) = (3,)  # если берём одну цифру, то необходимо ставить запятую.
# print(a)
# print(a[0])
# # в Терминале будет:
# # (3,)
# # 3
# # без запятой будет выдаваться ошибка.


# t = tuple(['red', 'green', 'blue'])
# print(t[0])         # red
# print(t[2])         # blue
# # print(t[10])      # IndexError: tuple index out of range
# print(t[-2])        # green
# # print(t[-200])    # IndexError: tuple index out of range

# for e in t:
#     print(e)     # red green blue
# t[0] = 'black'   # TypeError: 'tuple' object does not support item assignment

# a = (3, 4, 5)
# print (a)
# print(a[0])


# a = (3, 4, 5)
# for item in a:
#     print(item)
# # в Терминале будет:
# # 3
# # 4
# # 5


# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue


# # СЛОВАРИ
# # Неупорядоченные коллекции произвольных объектов с доступом по ключу.

# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# # print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# # print(dictionary['left'])  # ←

# # типы ключей могут отличаться.
# # Ключи:
# for k in dictionary.keys(): # для k в словаре.ключи - перевод с англ.
#     print(k)
# # в Терминале будут показаны ключи:
# # up
# # left
# # down
# # right


# # Конкретное значение:
# for k in dictionary.values(): # для k в словаре.значения - перевод с англ.
#     print(k)
# # в Терминале будет показаны значения:
# # ↑
# # ←
# # ↓
# # →

# # Если мы хотим пробежаться по всем элементам нашего словаря то:
# for v in dictionary:
#     print(v)
# # в Терминале будет показаны ключи:
# # up
# # left
# # down
# # right

# # Изменить ключ.
# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary['up'] )
# dictionary['up'] = 'up'
# print(dictionary['up'] )

# print(dictionary['up'])   # ↑
# # типы ключей могут отличаться

# # Удалить значение и ключ:
# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }

# del dictionary['left'] # удаление элемента

# for item in dictionary:       # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))

# # в Терминале будет без left: ←
# # up: ↑
# # down: ↓
# # right: →


# # МНОЖЕСТВА
# # Неупорядоченная совокупность элементов
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a))  # set
# print(type(b))  # set

# Множества
# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a))  # set
# print(type(b))  # set
# print(type(c))  # set
# a = {1, 1, 1, 1, 1}
# print(a)  # {1}

# Множества
# colors = {'red', 'green', 'blue'}  # цвета = {'красный', 'зеленый', 'синий'}
# print(type(colors))                # печать (цвета)
# # В Терминале будет:
# # <class 'set'>
# exit()    # позволяет не выполнять код, который ниже в скрипте прописан.

# # Множества
# colors = {'red', 'green', 'blue'}  # цвета = {'красный', 'зеленый', 'синий'}
# print(colors)          # печать (цвета): {'red', 'green', 'blue'}
# colors.add('red')      # цвета.добавить('красный'), т.к. онуже добавлен, он печататься не будет, но и ошибка не будет выходить.
# print(colors)          # {'red', 'green', 'blue'}
# colors.add('gray')     # цвета.добавить("серый")
# print(colors)          # {'red', 'green', 'blue','gray'}
# colors.remove('red')   # цвета.удалить("красный")
# print(colors)          # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red' (если попытаемся удалить элемент, которого нет, то будет ОШИБКА)
# colors.discard('red')  # цвета.отбросить('красный') # ok
# print(colors)          # печать (цвета) {'green', 'blue','gray'}
# colors.clear()         # цвета.очистить(): { } очистить множество и начать работать с множеством, с чистого листа.
# print(colors)          # set()


# # Множества (посмотреть в исходниках к этой лекции)
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()               # c = {1, 2, 3, 5, 8} - копировать (создать множество на основе имеющегося)
# u = a.union(b)             # u = {1, 2, 3, 5, 8, 13, 21} - если хотим сделать объединение множеств
# i = a.intersection(b)      # i = {8, 2, 5} - если требуется делать пересечение.
# dl = a.difference(b)       # dl = {1, 3} - разница
# dr = b.difference(a)       # dr = {13, 21} - разница 

# q = a\
#     .union(b) \
#     .difference(a.intersection(b))
# # {1, 21, 3, 13}    



# # Множества.
# # Неизменяемое множество:
# a = {1, 2, 3, 5, 8}
# b = frozenset(a) # b = замороженная
# print(b) # frozenset({1, 2, 3, 5, 8}) 
# # с англ. - печать (b) # замороженное множество ({1, 2, 3, 5, 8})
# # здесь уже никакие методы добавления или удаления работать не будут.




# # СПИСКИ (более глубокая теория со списками).
# # 1. Если у нас имеется list1  = и в нём лежат [1, 2, 3, 4, 5] какие-то значения.
# # И есть второй лист list2 = list1 (так делаем копию).
# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# for e in list1:
#     print(e)     # печать list1

# print()          # Вывод пустой строки

# for e in list2:
#     print(e)     # печать list2

# # В Терминале будет так:
# # 1
# # 2
# # 3
# # 4
# # 5

# # 1
# # 2
# # 3
# # 4
# # 5


# # 2. Съиграем в любопытную игру.
# list1 = [1, 2, 3, 4, 5]
# list2 = list1
 
# for e in list1:
#     print(e)     # печать list1

# print()          # Вывод пустой строки

# for e in list2:
#     print(e)     # печать list2
# print()
# # Поменяем значение первого элемента и поставим туда значение 123
# # И поменяются значения в обоих списках:
# list1[0] = 123
# # Поменяем значение второго списка и поставим туда значение 333:
# # И поменяются значения в обоих списках:
# list2[1] = 333
# # И снова распечатаем два списка:
# for e in list1:
#     print(e)     

# print()           

# for e in list2:
#     print(e)
# # в Терминале будет так: поменяются значения в обоих списках:
# # 1
# # 2
# # 3
# # 4
# # 5

# # 1
# # 2
# # 3
# # 4
# # 5

# # 123
# # 333
# # 3
# # 4
# # 5

# # 123
# # 333
# # 3
# # 4
# # 5

 
# # Функционал - это, каким образом можно удалять
# # последний элемент списка методом .pop
# list1 = [1, 2, 3, 4, 5]

# print(len(list1))   # будем сразу же печатать.
# print(list1.pop())  # сколько элементов теперь становится в списке.
# print(list1)        # печать оставшегося списка
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

# # Метод .pop извлекает последний элемент и список уменьшается.
# # в Терминале будет так:
# # 5
# # 5
# # [1, 2, 3, 4]
# # 4
# # [1, 2, 3]
# # 3
# # [1, 2]


# # Если нам нужно удалить какой-то кнкретный элемент из списка,то:
# list1 = [1, 2, 3, 4, 5]

# print(list1.pop(2))
# print(list1)
# # в Терминале будет так:
# # 3
# # [1, 2, 4, 5]


# # Если нам нужно вставить какой-то кнкретный элемент в список,то:
# list1 = [1, 2, 3, 4, 5]

# print(list1.insert(2, 11))
# print(list1)
# # в Терминале будет так:
# # None
# # [1, 2, 11, 3, 4, 5]


# Если нам нужно просто добавление в конец списка,то:
list1 = [1, 2, 3, 4, 5]

print(list1.append(11))
print(list1)
# в Терминале будет так:
# None
# [1, 2, 3, 4, 5, 11]
