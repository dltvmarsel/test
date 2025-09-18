import math

def f(x):
    try:
        numerator = x**2 - 15
        denominator = math.log(x**2) + 3*x - 7
        return numerator / denominator
    except (ValueError, ZeroDivisionError):
        return None

x0 = float(input("Введите начальное значение x0: "))
h = float(input("Введите шаг h: "))

x = x0
while True:
    y = f(x)
    if y is None:
        print(f"x={x:.3f} — точка разрыва или вне области определения")
        break
    print(f"x={x:.3f}, y={y:.3f}")

    # Проверка на характерные точки
    if abs(x**2 - 15) < 1e-6:  # нули числителя
        print("Достигнут ноль функции")
        break
    if abs(math.log(x**2) + 3*x - 7) < 1e-6:  # нули знаменателя
        print("Достигнута асимптота (знаменатель = 0)")
        break

    x += h
