# monday = int (input ('введите расходы за понедельник'))
# tuesday = int (input('введите расходы за вторник'))
# wednesday = int (input('введите расходы за среду'))
# thursday = int(input('введите расходы за четверг'))
# friday = int (input('введите расходы за пятницу'))
# saturday = int (input('введите расходы за субботу'))
# sanday = int (input('введите расходы за воскресенье'))
# total = monday + tuesday + wednesday + thursday + friday + saturday + sanday
# print('Общие расходы за неделю:',total)
# average = (total / 7)
# print(f'Средние расходы за день: {average:.1f}')
#
# if 1 <= average <= 200  :
#     print('eco')
# elif 201<= average <= 500 :
#     print('good')
# elif average >= 501 :
#     print('hard')
# else:
#     print('ничего не потрачено ')
# total = 0
# days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
# i = 0
# days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
# total = 0
# i = 0
# while i < 7:
#     expense = int(input(f'Введите расходы за {days[i]}: '))
#     total += expense
#     i += 1
# average = total / 7
# print('Общие расходы за неделю:', total)
# print(f'Средние расходы за день: {average:.1f}')
print("Программа управления светофором. Введите цвет или 'выход' для завершения.")

while True:
    color = input("Введите цвет светофора (зеленый, желтый, красный) или 'выход': ").lower()

    if color == "выход":
        print("Программа завершена.")
        break
    elif color == "зеленый":
        print("иди!")
    elif color == "желтый":
        print("подожди!")
    elif color == "красный":
        print("стой!")
    else:
        print("Неверный запрос! Пожалуйста, введите правильный цвет светофора или 'выход'.")
