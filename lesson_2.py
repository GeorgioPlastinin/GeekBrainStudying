# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

les_list = [1, 'текст', 2.15, True]
for elem in les_list:
    print(type(elem))

# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

les_list = input("Введите занчения через запятую: \n").split(',')
index = 0
for elem in les_list:
    try:
        les_list[index], les_list[index + 1] = les_list[index + 1], les_list[index]
        index += 2
    except IndexError:
        break
print(les_list)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

season = {"winter": {12, 1, 2}, "spring": {3, 4, 5}, "summer": {6, 7, 8}, "autumn": {9, 10, 11}} #решениче через словарь c исключением

try:
    month = int(input('Введите номер месяца от 1 до 12: '))
    if month < 1 or month > 12:
        raise ValueError
    else:
        for elem in season:
            if month in season.get(elem):
                print(elem)
except ValueError:
    print("Введи значение от 1 до 12!")



winter = [12, 1, 2] # решение через списки
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

month = int(input('Введите номер месяца от 1 до 12: '))
if month in winter:
    print("winter")
elif month in spring:
    print("spring")
elif month in summer:
    print("summer")
elif month in autumn:
    print("autumn")
else:
    print("Вы ввеил некорректный месяц!")

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

string = input("Введите текст: \n").split(' ')
str_num = 0
for elem in string:
    str_num += 1
    print("строка " + str(str_num) + ".", elem[0:10])


# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

scores = [7, 5, 3, 3, 2]
new_score = int(input("Введите новые число: \n"))
if new_score > max(scores):
    scores.insert(0, new_score)
elif new_score < min(scores):
    scores.append(new_score)
elif new_score in scores:
    index = scores.index(new_score)
    scores.insert(index, new_score)
elif new_score not in scores:
    index = 0
    for elem in scores:
        index += 1
        if new_score < elem:
            continue
        else:
            scores.insert(index - 1, new_score)
            break
print(scores)

# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# # В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# # Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

super_dicts = {}
while True: # самое удобное было бы реализовать через функции, и например sqlite или pickle, но мы их пока не проходили, по-этому так.
    print(
    """
    Нажмите (1), если вы хотите добавить товар;
    Нажмите (2), если вы хотите провести аналитику, уже выбранных товаров;
    Нажмите (0), чтобы выйти.
    """)

    choise = int(input("Ваш выбор: \n"))
    if choise == 0:
        break
    elif choise == 1:
        goods_number = int(input("Введите номер(артикул) товара: \n"))
        goods_name = input("Введите название товара: \n")
        goods_price = int(input("Введите цену товара в рублях без копеек: \n"))
        goods_count = int(input("Введите кол-во выбранного товара: \n"))
        goods_unit = input("Введите единицу измерения: \n").lower()

        goods = (goods_number, {'название': [goods_name], 'цена': [goods_price], 'количество': [goods_count], 'ед': [goods_unit]})
        if super_dicts == {}:
            super_dicts.update(goods[1])
        else:
            super_dicts['название'].append(goods_name)
            super_dicts['цена'].append(goods_price)
            super_dicts['количество'].append(goods_count)
            super_dicts['ед'].append(goods_unit)
    elif choise == 2:
        print(super_dicts)
