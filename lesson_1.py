#тренировка пулреквостов

# Задание 1
number = 1
string = 'str'
float_number = 1.123
boolean = True

print(number, string, float_number, boolean)

number = int(input('Введите число: '))
string = input('Введите текст: ')
float_number = float(input('Введите число с дробной \".\": '))
boolean = (number > int(float_number))

print(number, string, float_number)
print('Число больше дробного числа? - ', boolean)

# Задание 2
seconds = int(input("Введите кол-во секуд целым числом: "))

seconds = seconds % (24 * 3600)
hour = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

print("%d:%02d:%02d" %(hour, minutes, seconds))

# Задание 3 //странная работа с числами выше 10 (я бы доработал условие задачи)
number = int(input('Введите число: '))

number1 = number
number2 = number + number
number3 = number + number + number

print(int(number1) + int(number2) + int(number3))

# Задача 4 // не придумал как решить задачу через цикл while
number = input("Введите число, а я найду самую большую цифру в числе: ")
print(max(number))

# Задача 5
income = int(input('Введите доход в рублях (целое число): '))
cost = int(input('Введите расходы в рублях (целое число): '))

if income > cost:
    print('Фирма заработала: ', income - cost, '. Рентабельность составила: ', (income/cost * 100), '%')
    personal = int(input('Введите кол-во персонала числом: '))
    print('Выручка на сотрудника составила: ', int((income - cost) / personal), ' рублей.')
else:
    print("Фирма работает в убыток!!!")

# Задача 6
a = 2
b = 3
days = 1

while a < b:
    a = a + (a * 0.1)
    days += 1
    print("День ", days, ": Результат: {0:.2f}".format(a))