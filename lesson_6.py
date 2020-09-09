import time
from itertools import cycle
import random

"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
 Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
 красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
 второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
 Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
 Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.
"""


# class TrafficLight:
#     __color = ['Красный', 'Жёлтый', 'Зеленый']
#
#     def __init__(self):
#         print('Запуск светофора! \n')
#
#     def running(self, count=None):
#         switching = TrafficLight.__color
#         try_count = 0
#         for elem in cycle(switching):
#             if elem == 'Красный' and switching[1] == 'Жёлтый':
#                 print(elem), time.sleep(7)
#             elif elem == 'Жёлтый' and switching[2] == 'Зеленый':
#                 print(elem), time.sleep(2)
#             elif elem == 'Зеленый' and switching[0] == 'Красный':
#                 print(elem), time.sleep(5)
#                 try_count += 1
#                 if try_count == count and count is not None:
#                     break
#             else:
#                 print('Это не рабочий светофор!')
#                 break
#
#
# light = TrafficLight()
# light.running(2)  # реализовал количество повторений, так как в основе лежит cycle


"""Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. 
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна 
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число 
см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


# class Road:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def calculation(self, mass, depth):
#         return self._length * self._width * mass * depth
#
#
# r = Road(10, 10)
# print(r.calculation(10, 10))


"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), 
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, 
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода 
с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, 
передать данные, проверить значения атрибутов, вызвать методы экземпляров)."""


# class Worker:
#     name = 'Георгий'
#     surname = 'Александроич'
#     position = 'Python Developer'
#     _income = {"wage": 100, "bonus": 500}
#
#
# class Position(Worker):
#     def get_full_name(self):
#         return Worker.name + ' ' + Worker.surname
#
#     def get_total_income(self):
#         return sum(dict.values(self._income))
#
#
# p = Position()
# print(p.get_full_name())
# print(p.position)
# print('Доход: {}'.format(p.get_total_income()))


"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).  
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, 
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат.
"""


class Car:  # На самом деле тут можно играться до бесконечности, и создать гонку. К тому же, опеределение класса машин,
    # лучше всего делать в одном классе, а остальные - class Road и переплетать взаимодействия.

    __direction = ['Left', 'Right', 'Backward']

    def __init__(self, speed=0, color='red', name=None, is_police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

        if is_police == True:
            self.name = 'Полиция'

    def go(self):
        print('Машина {} имеющая цвет - {} начинает движение'.format(self.name, self.color))
        try:
            self.speed = int(input('Переключатель скоростей. Введите вашу скорость: \n'))
            self.show_speed()
            if self.speed == 0:
                self.stop()

        except ValueError:
            print("Введите скорость целым числом!")


    def stop(self):
        print('Машина остановилась')
        self.speed = 0

    def turn(self):
        print('Машина {} повернула - {}'.format(self.name, random.choice(self.__direction))) \
            if self.speed > 0 else print("Машина стоит!")

    def show_speed(self):
        print('Текущая скорость: {}'.format(self.speed))

class TownCar(Car):

    def show_speed(self):
        print('Скорость {}: {}'.format(self.name, self.speed))
        if self.speed > 60:
            print('Превышение скорости! Снизте скорость!')

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        print('Скорость {}: {}'.format(self.name, self.speed))
        #print('Текущая скорость: {}'.format(TownCar.speed))
        if self.speed > 40:
            print('Превышение скорости! Снизте скорость!')

class Police(Car):
    pass

wc = WorkCar(color='black and yellow', name='taxi')
tc = TownCar(color='silver', name='toyota')
sc = SportCar(name='ferrari')
p = Police(color='white and blue', is_police=True)

wc.go()
tc.go()
sc.go()
p.go()

wc.turn()
tc.turn()
sc.turn()
p.turn()


"""Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) 
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), 
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из 
классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный 
метод для каждого экземпляра."""

# class Stationery:
#
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         print('Запуск отрисовки!')
#
# class Pen(Stationery):
#
#
#     def draw(self):
#         print('Запуск отрисовки предметом - {}'.format(self.title))
#
#
# class Pencil(Stationery):
#
#     def draw(self):
#         print('Предметом {} рисуешь ты'.format(self.title))
#
#
# class Handle(Stationery):
#
#     def draw(self):
#         print('А это жирный {}'.format(self.title))
#
#
# p = Pen('Ручка')
# pc = Pencil('Карандаш')
# h = Handle('Маркер')
#
# p.draw()
# pc.draw()
# h.draw()

