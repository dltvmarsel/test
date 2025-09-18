# Написать функцию “ближайшее число”
first_task = " Функция “ближайшее число”"
print(first_task)
def nearest_number(numbers, target):

    numbers = list(numbers)
    sorted_numbers = sorted(numbers, key=lambda x: abs(x - target))
    nearest = sorted_numbers[0]

    return nearest, sorted_numbers

nums = [10, 2, 15, 7, 3.5]
target = 8
print(nearest_number(nums, target))

 # Напишите примеры использования lambda функций с такими функциями как filter, map по одному примеру на своё усмотрение.

second_task  = "Примеры использования lambda функций с такими функциями как filter, map по одному примеру на своё усмотрение."
print(second_task)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)

#  Создать функцию для вывода элемента списка/кортежа/строки (iterable) по указанному индексу.
def get_element(data=[1, 2, 3, 4, 5]):
    last_index = len(data) - 1
    print(f"Можно вводить индексы от 0 до {last_index}. Для выхода напишите 'exit'.")

    while True:
        idx = input("Введите индекс: ")

        if idx.lower() == "exit":
            print("Программа завершена.")
            break

        try:
            idx = int(idx)
            print(f"Элемент под индексом {idx}: {data[idx]}")
        except (ValueError, TypeError):
            print("Нужно ввести число или 'exit'.")
        except IndexError:
            print(f"Такого индекса нет. Доступные индексы: 0 … {last_index}")
get_element("Python")


