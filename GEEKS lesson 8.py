#Контекстны менеджер 'with' работа с файлами
# w - write()
# a - add()
# x - (пересечение одного файла, запись с проверкой названия)
# file = open('new_file.txt','w')
# file.write('Bishkek, Kyrgyzstan.')
# file.close()


# with open('new_file.txt','a') as file:
#     file.write('\n dobavlaem stroku')

# with open('lol_file.txt','x') as new:
#      new.write('new file new Data!')

from time import sleep

with open('new_file.txt','r') as file:
     for symbol in file.read():
         print(symbol.title(), end='')
         if symbol == ' ':
             continue
         sleep(1)

    # print(file.read().index('ы'))
    # print(file.read()[23])
    # print(len(file.read()))
    # print(file.readlines()[-1])
