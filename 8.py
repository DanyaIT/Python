# Задание 1.
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# [[], [], []]
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции
# сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.
# Пример:
# 1 2 3
# 4 5 6
# 7 8 9
#
# 1 2 3
# 4 5 6
# 7 8 9
# Сумма матриц:
# 2 4 6
# 8 10 12
# 14 16 18


class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        print('\n'.join(list(map(str, self))))

    def __add__(self, other):
        self.other = other
        for i in range(len(self.my_list)):
            for j in range(len(self.my_list[i])):
                other[i][j] = other[i][j] + self.my_list[i][j]
        return Matrix.__str__(other)


matrix = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
matrix.__add__([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])


# Задание 2
# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка (Cell).
# В его конструкторе инициализировать параметр (quantity),
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (add()),
# вычитание (sub()),
# умножение (mul()),
# деление (truediv()).


class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return f'Сумма: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        if sub > 0:
            return f'Разность: {sub}'
        else:
            return 'Вы уничтожили клетку('

    def __mul__(self, other):
        return f'Произведение: {self.quantity * other.quantity}'

    def __truediv__(self, other):
        return f'Деление: {self.quantity // other.quantity}'

    def make_order(self, row):
        my_str = ''
        for i in range(int(self.quantity / row)):
            my_str += f'{"^" * row}\n'
        my_str += f'{"^" * (self.quantity % row)}\n'
        return my_str


ceil_1 = Cell(31)
ceil_2 = Cell(9)
print(ceil_1 + ceil_2)
print(ceil_1 - ceil_2)
print(ceil_1 * ceil_2)
print(ceil_1 / ceil_2)
print(ceil_1.make_order(5))


# Задание 3.
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Zero:
    def __init__(self, divisible, divider):
        self.divisible = divisible
        self.divider = divider

    def share_on_zero(self):
        try:
            return round(self.divisible / self.divider)
        except:
            return 'Вы еще не освоили выш. мат.!'


zero = Zero(15, 5)
print(zero.share_on_zero())
print(Zero(100, 0).share_on_zero())
