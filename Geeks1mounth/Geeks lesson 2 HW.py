while True:
    try:
        day = (input("Введите день рождения (1-31): "))
        if day == 'stop':
            break
        month = int(input("Введите месяц рождения (1-12): "))

        valid: bool = False
        if month == 1 <= day <= 31:
            valid = True
        elif month == 2 and 1 <= day <= 29:
            valid = True
            if day == 29:
                print("Примечание: 29 февраля бывает только в високосный год.")
        elif month == 3 and 1 <= day <= 31:
            valid = True
        elif month == 4 and 1 <= day <= 30:
            valid = True
        elif month == 5 and 1 <= day <= 31:
            valid = True
        elif month == 6 and 1 <= day <= 30:
            valid = True
        elif month == 7 and 1 <= day <= 31:
            valid = True
        elif month == 8 and 1 <= day <= 31:
            valid = True
        elif month == 9 and 1 <= day <= 30:
            valid = True
        elif month == 10 and 1 <= day <= 31:
            valid = True
        elif month == 11 and 1 <= day <= 30:
            valid = True
        elif month == 12 and 1 <= day <= 31:
            valid = True

        if valid:
            # Определение знака зодиака
            if (day >= 21 and month == 3) or (day <= 20 and month == 4):
                print("Ваш знак зодиака: Овен")
            elif (day >= 21 and month == 4) or (day <= 20 and month == 5):
                print("Ваш знак зодиака: Телец")
            elif (day >= 21 and month == 5) or (day <= 21 and month == 6):
                print("Ваш знак зодиака: Близнецы")
            elif (day >= 22 and month == 6) or (day <= 22 and month == 7):
                print("Ваш знак зодиака: Рак")
            elif (day >= 23 and month == 7) or (day <= 22 and month == 8):
                print("Ваш знак зодиака: Лев")
            elif (day >= 23 and month == 8) or (day <= 22 and month == 9):
                print("Ваш знак зодиака: Дева")
            elif (day >= 23 and month == 9) or (day <= 22 and month == 10):
                print("Ваш знак зодиака: Весы")
            elif (day >= 23 and month == 10) or (day <= 22 and month == 11):
                print("Ваш знак зодиака: Скорпион")
            elif (day >= 23 and month == 11) or (day <= 21 and month == 12):
                print("Ваш знак зодиака: Стрелец")
            elif (day >= 22 and month == 12) or (day <= 20 and month == 1):
                print("Ваш знак зодиака: Козерог")
            elif (day >= 21 and month == 1) or (day <= 18 and month == 2):
                print("Ваш знак зодиака: Водолей")
            elif (day >= 19 and month == 2) or (day <= 20 and month == 3):
                print("Ваш знак зодиака: Рыбы")
        else:
            print("Ошибка: Введена несуществующая дата. Проверьте правильность  написания дня и месяца.")
    except ValueError:
        print("Ошибка: Введите числовые значения для дня и месяца.")
