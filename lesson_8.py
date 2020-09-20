from datetime import datetime
import sqlite3

"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и 
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и 
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""

# class Date:
#     def __init__(self, date):
#         self.date = date
#
#     @classmethod
#     def numeric(cls, date):
#         for elem in date.split('-'):
#             yield int(elem)
#
#     @staticmethod
#     def validate(date):
#         try:
#             datetime.strptime(date, '%d-%m-%Y')
#             print('Дата верна!')
#         except ValueError:
#             print('Некорректный формат даты, либо дата не верна!')
#
#
# date_iso = datetime.strftime(datetime.now(), '%d-%m-%Y')  # для более легких значений, использовал модуль datetime
# # date_iso = input('Введите дату в формате \'ДД-ММ-ГГГГ\':\n')
# print(list(Date.numeric(date_iso)))
# Date.validate(date_iso)

"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться 
с ошибкой.
"""

# class Exp(Exception):
#
#     def __init__(self):
#         print('Вы поделили на ноль!')
#
#
# data = int(input("Введите ноль: "))
#
# try:
#     if data == 0:
#         raise Exp()
# except Exp:
#     print('Вселенная схлопнулась!')
# else:
#     print('Вы не поделили на ноль! Вселенная спасена!')


"""Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список 
только числами. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу 
скрипта, введя, например, команду “stop”. 
При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
 При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, 
 только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) 
 и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться."""

# class ThisIsNotNumber(Exception):
#     def __init__(self, err_text):
#         self.err_text = err_text
#
#
# #raise ThisIsNotNumber('Вы ввели текстовый символ!')
# class Validator:
#
#     my_list = []
#
#     @staticmethod
#     def validate(data):
#         try:
#             Validator.check(data)
#             Validator.my_list.append(data)
#         except ThisIsNotNumber:
#             print('Вы ввели не число!')
#
#     def __str__(self):
#         return Validator.my_list
#
#     @classmethod
#     def check(cls, data):
#         try:
#             data = int(data)
#         except ValueError:
#             raise ThisIsNotNumber('Вы ввели текстовый символ!')
#
#
# data = ''
# while True:
#     data = input('Введите символ:\n')
#     if data == 'stop':
#         print(Validator.my_list)
#         break
#     else:
#         Validator.validate(data)


""" Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
 общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
 
Продолжить работу над первым заданием. 
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно 
использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, 
изученных на уроках по ООП."""


class Main:
    input_choise = ''
    while input_choise != 'stop':
        input_choise = input("""
        Перед вами симулятор работы склада, написанный по принципам ООП, с использованием знаний,
        полученных на предыдущих уроках. Для того, чтобы выйти из симулятора - напишите \"stop\"
        
        Меню:
        1 -- Проверка скалада;
        2 -- Добавить товар на склад;
        3 -- Списать товар со склада;
        4 -- Передать товар подразделению "компании".
        """).lower()

class DataValidator:
    pass


class StoreHouse:
    def __init__(self, base='lesson_8db.db'):
        self.connection = sqlite3.connect(base)
        self.cursor = self.connection.cursor()

    def expect_storehouse(self):
        self.cursor.execute('SELECT Name, TechCount FROM supplies')

    def write_supplies(self):
        pass

    def remove_supplies(self):
        pass


class OfficeAppliances:
    def __init__(self, model, model_name, tech_count):
        self.model = model
        self.model_name = model_name
        self.tech_count = tech_count

    def send_to_storehouse(self):
        consideration_list = [self.model_name, self.tech_count]
        #Storehouse.supplies_dictionaty['%s']['Model'].append(consideration_list) % self.model

    def remove_from_storehouse(self):
        pass


class Printer(OfficeAppliances):
    pass


class Scanner(OfficeAppliances):
    pass


class Xerox(OfficeAppliances):
    pass


"""7. == Лото ==."""
