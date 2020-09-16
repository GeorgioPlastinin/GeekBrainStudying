import random
from abc import ABC, abstractmethod

"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д."""

class Matrix:
    def __init__(self, matrix_length=random.randrange(1, 6), matrix_width=random.randrange(1, 6)):
            self.matrix_length = matrix_length
            self.matrix_width = matrix_width
            self.matrix = [[random.randrange(0, 10) for y in range(matrix_length)] for x in range(matrix_width)]

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % el for el in elem]) for elem in self.matrix])

    def __add__(self, other):
        if other.matrix_length != self.matrix_length or other.matrix_width != self.matrix_width:
            print('Матрицы разного размера!')
        else:
            for m_1_elem, m_2_elem in zip(self.matrix, other.matrix):
                new_matrix = list(map(lambda x, y: x + y, m_1_elem, m_2_elem))
                print('\t'.join(['%d' % el for el in new_matrix]))


m_1 = Matrix(3, 3)
m_2 = Matrix(3, 3)

print(m_1, '\n')
print(m_2, '\n')

m_1 + m_2

"""Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
 — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. 
 У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: 
 V и H, соответственно. 
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H 
+ 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

class Abstract(ABC):
    @abstractmethod
    def suit(self):
        pass

    @abstractmethod
    def coat(self):
        pass
# Все понятно, но нет смысла наследоваться от Abstract
class Suit():
    def __init__(self, growth):
        self.growth = growth

    @property
    def suit(self):
        suit_growth = 2 * self.growth + 0.3
        return suit_growth


class Coat():
    def __init__(self, size):
        self.size = size

    @property
    def coat(self):
        coat_size = self.size / 6.5 + 0.5
        return coat_size


coat = Coat(45)
suit = Suit(184)

print("Метров ткани понадобиться: ", coat.coat + suit.suit)

"""3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. 
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны 
быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), 
умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять 
увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления 
должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих 
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества 
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
 *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: 
*****\n*****\n*****."""

class Cell:
    def __init__(self, count):
        try:
            self.count = int(count)
        except ValueError:
            print('Введите целое число для формирования клетки!')

    def __add__(self, other):
        return self.count + other.count

    def __sub__(self, other):
        return self.count - other.count if (self.count - other.count) > 0 else print('Клетки меньше нуля!')

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return self.count // other.count

    def make_order(self, torch_count):
        cell_count = ''
        while self.count != 0:
            cell_count += '*'
            if cell_count.count('*') % torch_count == 0:
                cell_count += '\\n'
            self.count -= 1

        return cell_count



critter = Cell(6)
critter_2 = Cell(5)

print(critter - critter_2, critter + critter_2, critter * critter_2, critter / critter_2)

print(Cell.make_order(critter, 5))
