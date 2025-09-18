low, high = 1, 100
attempts, history = 0, []

print("Загадай число от 1 до 100. Отвечай: да / больше / меньше.")

while low <= high:
    guess = (low + high) // 2
    attempts += 1
    history.append(guess)

    ans = input(f"Твое число {guess}? ").strip().lower()

    if ans == "да":
        print(f"Угадал за {attempts} попыток! Число: {guess}")
        with open("results.txt", "w", encoding="utf-8") as f:
            f.write(f"Число: {guess}\nПопытки: {attempts}\nИстория: {history}\n")
        break
    if ans == "больше": low = guess + 1
    elif ans == "меньше": high = guess - 1
    else: print("Введи: да / больше / меньше.")
else:
    print("Где-то ошибка в ответах :)")

