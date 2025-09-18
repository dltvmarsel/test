# Операторы: принадлежности, назначения, циклы.

"""Оператор принадлежности in"""

#
# print('n' in 'pyton')
# print('l' in 'pyton')
#
# print(2 in range(1, 6))
# print(22 in range(1, 11))


"""Операторы принадлежности"""
# number = 5
# number = number + 4
#  number = number - 2
# number += 4
# number -= 2
# number **= 2
# print(number)


"""цикл while"""
#
# counter = 5
# while counter > 0:
#     time = input().lower()
#
#     if time ==  'morning'or time == 'утро':
#         print('good morning')
#     elif time == 'day'or time == 'день':
#         print('good afternoon')
#     elif time == 'evning' or time == 'вечер':
#         print('good evning')
#     else:
#         print('hello')
#     counter -=1
#     print(f'ostalos {counter} popytok')
#



counter = int(input('ukazhyte kolichestvo popytok'))
while counter > 0:
        time = input().lower()

        if time == 'morning' or time == 'утро':
            print('good morning')
        elif time == 'day' or time == 'день':
            print('good afternoon')
        elif time == 'evning' or time == 'вечер':
            print('good evning')
        else:
            print('hello')
        counter -= 1
        print(f'ostalos {counter} popytok')

"""цикл for """
# word ='kyrgyzstan'
# for letter in word:
#     if letter == 's':
#         break
#     if letter in 'yr':
#         continue
#     print(letter)
#
# cash = 100
# percents = 0.1
# years = 5
# for year in range(1,years+1):
#     cash += cash * percents
#     cash = round(cash,2)
#     print(f'{year}){cash}')
#


