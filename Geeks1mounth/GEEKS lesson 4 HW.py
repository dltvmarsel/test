data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

# Разделяем строки и числа
for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)

numbers.remove(6.13)
numbers.remove(True)
letters.append(True)

numbers.insert(1, 2)
numbers.sort()

letters.reverse()
letters[1] = 'G'
letters[6] = 'c'

numbers = [n**2 for n in numbers]

letters = tuple(letters)
numbers = tuple(numbers)

print(letters)
print(numbers)
