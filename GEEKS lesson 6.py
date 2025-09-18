# Функции: виды параметров, возвращение данных, виды аргументов.
# DRY - don't repeat yourself
# define - определить

# *args, **kwargs

"""из чего состоит функция?"""
# определение(def) наименование(параметры):
#     тело функции
#     возвращение результата (return)
#
# наименование(аргументы) вызов функции


# name - required positional parameter
# surname - non-required positional parameter
# def some_name(name, surname='неизвестно'):  # name, surname - это параметры
#     print(f'name: {name} surname: {surname}')
#
# some_name('chyngyz', 'aitmatov')  # - это аргументы
# some_name('pushkin', 'aleksandr')
# some_name(surname='pushkin', name='aleksandr')  # ключевые аргументы
# some_name()

# some_name()
# some_name()

# def get_square(length: int, width: int) -> int:
#     """Принимает длину и ширину, возвращает площадь."""
#     return length * width

# print(get_square.__doc__)
# print(help(get_square))

# print(len.__doc__)
# print(help(len))

# square_2 = get_square(7, 5)
# square_victory = get_square(420, 240)
#
# print(square_2)
# print(square_victory)

# length = 7
# width = 5
# square_2 = length * width
# print(square_2)
#
# length = 420
# width = 240
# square_victory = length * width
# print(square_victory)

# from random import choice
# students = [9, 15, 16, 11, 14, 17, 2, 10, 6, 1, 4, 7, 3]
# results = {}
#
# while students:
#     student_id = choice(students)
#     name = input(f'enter student name {student_id}: ').title()
#     rate = int(input(f'enter rate for {name}: '))
#     results[name] = rate
#     students.remove(student_id)
#
# average_rate = sum(results.values()) / len(results)
# print(results)
# print(average_rate)
