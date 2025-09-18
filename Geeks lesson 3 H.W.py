counter = int(input("Укажите количество попыток: "))

VOWELS = "аеёиоуыэюяaeiou"
RUS_LETTERS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ENG_LETTERS = "abcdefghijklmnopqrstuvwxyz"

while counter > 0:
    word = input("Введите слово (латиница или кириллица, stop для выхода): ").strip().lower()

    if word == "stop":
        print("Выход из программы.")
        break

    # Проверка на недопустимые символы
    if not all(ch.isalpha() for ch in word):
        print("Ошибка: в слове должны быть только буквы!")
        counter -= 1
        print(f"Осталось {counter} попыток\n")
        continue

    # Считаем только буквы
    letters = [ch for ch in word if ch.isalpha()]
    total_letters = len(letters)

    if total_letters == 0:
        print("В слове нет букв.")
    else:
        vowel_count = sum(ch in VOWELS for ch in letters)
        consonant_count = total_letters - vowel_count  

        # Счётчики английских и русских букв
        rus_count = sum(ch in RUS_LETTERS for ch in letters)
        eng_count = sum(ch in ENG_LETTERS for ch in letters)

        vowel_percent = (vowel_count / total_letters) * 100
        consonant_percent = (consonant_count / total_letters) * 100

        print(f"Общее количество букв: {total_letters}")
        print(f"Гласных: {vowel_count}")
        print(f"Согласных: {consonant_count}")
        print(f"Английских букв: {eng_count}")
        print(f"Русских букв: {rus_count}")
        print(f"Процент гласных: {vowel_percent:.2f}%")
        print(f"Процент согласных: {consonant_percent:.2f}%")

    counter -= 1
    print(f"Осталось {counter} попыток\n")
