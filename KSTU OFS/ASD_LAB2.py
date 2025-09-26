MAX_SIZE = 100  # размер статического списка

def initialize():
    return [], 0  # пустой список и размер 0

def is_empty(size):
    return size == 0

def is_full(size):
    return size >= MAX_SIZE

def print_list(arr, size):
    if is_empty(size):
        print("Список пуст.")
    else:
        print("Список:", arr[:size])

# --- Добавление ---
def add_by_position(arr, size, pos, value):
    if is_full(size):
        print("Список переполнен!")
        return size
    if pos < 0 or pos > size:
        print("Некорректная позиция!")
        return size
    arr.insert(pos, value)
    return size + 1

def add_after_position(arr, size, pos, value):
    return add_by_position(arr, size, pos + 1, value)

def add_before_position(arr, size, pos, value):
    return add_by_position(arr, size, pos, value)

def add_by_value(arr, size, target, value):
    if target not in arr[:size]:
        print("Элемент не найден!")
        return size
    index = arr.index(target)
    return add_by_position(arr, size, index, value)

def add_after_value(arr, size, target, value):
    if target not in arr[:size]:
        print("Элемент не найден!")
        return size
    index = arr.index(target)
    return add_by_position(arr, size, index + 1, value)

def add_before_value(arr, size, target, value):
    if target not in arr[:size]:
        print("Элемент не найден!")
        return size
    index = arr.index(target)
    return add_by_position(arr, size, index, value)

# --- Удаление ---
def delete_by_position(arr, size, pos):
    if is_empty(size):
        print("Список пуст!")
        return size
    if pos < 0 or pos >= size:
        print("Некорректная позиция!")
        return size
    arr.pop(pos)
    return size - 1

def delete_after_position(arr, size, pos):
    return delete_by_position(arr, size, pos + 1)

def delete_before_position(arr, size, pos):
    return delete_by_position(arr, size, pos - 1)

def delete_by_value(arr, size, value):
    if value not in arr[:size]:
        print("Элемент не найден!")
        return size
    arr.remove(value)
    return size - 1

def delete_after_value(arr, size, value):
    if value not in arr[:size]:
        print("Элемент не найден!")
        return size
    index = arr.index(value)
    return delete_by_position(arr, size, index + 1)

def delete_before_value(arr, size, value):
    if value not in arr[:size]:
        print("Элемент не найден!")
        return size
    index = arr.index(value)
    return delete_by_position(arr, size, index - 1)

# --- Поиск ---
def find_by_position(arr, size, pos):
    if pos < 0 or pos >= size:
        print("Некорректная позиция!")
        return None
    return arr[pos]

def find_by_value(arr, size, value):
    if value in arr[:size]:
        return arr.index(value)
    else:
        return None

# --- Дополнительные функции ---
def find_min_position(arr, size):
    if is_empty(size):
        print("Список пуст!")
        return None
    min_val = min(arr[:size])
    return arr.index(min_val)

def sort_list(arr, size):
    arr[:size] = sorted(arr[:size])
    print("Список отсортирован.")

def clear_list():
    return [], 0

# --- Главное меню ---
def main():
    arr, size = initialize()

    while True:
        print("\nМеню:")
        print("1. Показать список")
        print("2. Добавить элемент")
        print("3. Удалить элемент")
        print("4. Найти элемент")
        print("5. Найти позицию минимального элемента")
        print("6. Отсортировать список")
        print("7. Очистить список")
        print("0. Выход")

        choice = input("Выбор: ")

        if choice == "1":
            print_list(arr, size)

        elif choice == "2":
            val = int(input("Введите значение: "))
            print("1. По позиции\n2. После позиции\n3. Перед позицией\n4. По значению\n5. После значения\n6. Перед значением")
            ch = input("Выбор: ")
            if ch == "1":
                pos = int(input("Позиция: "))
                size = add_by_position(arr, size, pos, val)
            elif ch == "2":
                pos = int(input("Позиция: "))
                size = add_after_position(arr, size, pos, val)
            elif ch == "3":
                pos = int(input("Позиция: "))
                size = add_before_position(arr, size, pos, val)
            elif ch == "4":
                target = int(input("Элемент: "))
                size = add_by_value(arr, size, target, val)
            elif ch == "5":
                target = int(input("Элемент: "))
                size = add_after_value(arr, size, target, val)
            elif ch == "6":
                target = int(input("Элемент: "))
                size = add_before_value(arr, size, target, val)

        elif choice == "3":
            print("1. По позиции\n2. После позиции\n3. Перед позицией\n4. По значению\n5. После значения\n6. Перед значением")
            ch = input("Выбор: ")
            if ch == "1":
                pos = int(input("Позиция: "))
                size = delete_by_position(arr, size, pos)
            elif ch == "2":
                pos = int(input("Позиция: "))
                size = delete_after_position(arr, size, pos)
            elif ch == "3":
                pos = int(input("Позиция: "))
                size = delete_before_position(arr, size, pos)
            elif ch == "4":
                val = int(input("Значение: "))
                size = delete_by_value(arr, size, val)
            elif ch == "5":
                val = int(input("Значение: "))
                size = delete_after_value(arr, size, val)
            elif ch == "6":
                val = int(input("Значение: "))
                size = delete_before_value(arr, size, val)

        elif choice == "4":
            print("1. По позиции\n2. По значению")
            ch = input("Выбор: ")
            if ch == "1":
                pos = int(input("Позиция: "))
                print("Элемент:", find_by_position(arr, size, pos))
            elif ch == "2":
                val = int(input("Значение: "))
                pos = find_by_value(arr, size, val)
                if pos is not None:
                    print(f"Элемент {val} найден на позиции {pos}")
                else:
                    print("Элемент не найден.")

        elif choice == "5":
            pos = find_min_position(arr, size)
            if pos is not None:
                print(f"Минимальный элемент {arr[pos]} на позиции {pos}")

        elif choice == "6":
            sort_list(arr, size)

        elif choice == "7":
            arr, size = clear_list()
            print("Список очищен.")

        elif choice == "0":
            break
        else:
            print("Некорректный выбор!")

if __name__ == "__main__":
    main()

