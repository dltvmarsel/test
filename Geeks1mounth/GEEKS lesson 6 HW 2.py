def nearest_number(sequence, target=0):
    closest = sequence[0]
    min_diff = abs(sequence[0] - target)

    for num in sequence:
        diff = abs(num - target)
        if diff < min_diff:
            min_diff = diff
            closest = num
    return closest


numbers = [1, 2, 3, 10, 7]

while True:
    try:
        target_input = float(input("Введите целевое число: "))
        result = nearest_number(numbers, target_input)
        print(f"Ближайшее число к {target_input}: {result}")
    except ValueError:
        print("Ошибка! Введите число правильно.")
