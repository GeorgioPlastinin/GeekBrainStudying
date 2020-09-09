"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

lines = 5 #указываем кол-во линиий (5 по дефолту)
def str_list(lines=5):
    for num, elem in enumerate(range(1, lines + 1), 1):
        elem = "Строка #" + str(num) + '\n'
        yield elem

with open("task_1.txt", 'r+', encoding='UTF-8') as file:
    file.writelines(str_list(lines))

print('Строки записаны! Смотри файл - \"task_1.txt\"')

"""Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке."""

with open("task_2.txt", 'r', encoding='UTF-8') as file:
    for num, line in enumerate(file, 1):
        print(num, line.rstrip('\n'))
    print('\nВсего строк: ', num)


"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников 
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., 
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

Пример файла:
Иванов 23543.12
Петров 13749.32
"""

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

with open("task_3.txt", 'r', encoding='UTF-8') as file:
    content = [line.rstrip('\n').split() for line in file]

numbers = []
names = []

for elem in content:
    numbers.append(float(elem[1]))
    if float(elem[1]) < 20000:
        names.append(elem[0])
print('Cредняя з/п: ', mean(numbers))
print(names)

"""Создать (не программно) текстовый файл со следующим содержимым: 
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""

replace_values = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}


def replace():
    with open("task_4.txt", 'r', encoding='UTF-8') as file:
        for line in file:
            replace_elem = line.split()[0]
            content = (line.rstrip('\n').replace(replace_elem, replace_values.get(replace_elem))) + '\n'
            yield content


with open("task_4_new.txt", 'w', encoding='UTF-8') as new_file:
    new_file.writelines(replace())

print('Замена произведена! Смотри файл - \"task_4_new.txt\"')

"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random
numbers = [str(elem) for elem in range(random.randrange(1, 100))]

with open("task_5.txt", 'w+', encoding='UTF-8') as file:
    file.write(' '.join(numbers))

with open("task_5.txt", 'r', encoding='UTF-8') as file:
    content = file.read().split()
    content_for_sum = [int(elem)for elem in content]

print(sum(content_for_sum))

"""Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
 практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета 
 не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество 
 занятий по нему. Вывести словарь на экран.
 
Примеры строк файла:                    Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

lessons_list = []
lessons_hours = []

def only_num(text):
    numbers = []
    cur_elem = ""
    for elem in str(text):
        try:
            elem = int(elem)
            cur_elem = cur_elem + str(elem)
        except:
            if cur_elem == "":
                continue
            numbers.append(int(cur_elem))
            cur_elem = ""
    return numbers

with open("task_6.txt", 'r', encoding='UTF-8') as file:
    for elem in file:
        lessons_list.append(elem.split(':')[0])
        lessons_hours.append(sum(list(only_num(elem.split()))))

print(dict(zip(lessons_list, lessons_hours)))

"""Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные 
о фирме: название, форма собственности, выручка, издержки. 
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков). 

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

firm_name = []
income = []


with open("task_7.txt", 'r', encoding='UTF-8') as file:
    for line in file:
        money = int(line.split()[2]) - int(line.split()[3])
        print('Прибыль компании ' + line.split()[0] + ': ' + str(money))
        if money > 0:
            firm_name.append(line.split()[0])
            income.append(money)

    # не включены, те кто в минусе
    dictionary = dict(zip(firm_name, income))
    average = mean(list(dictionary.values()))

    js = json.dumps([dictionary, {"average_profit": average}])
    print(js)
