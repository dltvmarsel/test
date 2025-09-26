#словари - dict,  множества
# {key value}
student = {
    'name': "adil",
    'age ': 18
}
"""dobavlenie"""
student['weight'] = 68.3
student.update({'country':'kg', 'height': 178})
print(student)

"""izmenenia"""
student['age'] = 19
print(student)
"""udalenie"""
student.pop('countru')
del student['weight']
print(student)
"""vyvod slovara v stolbik cherez cicle for"""
for i in student:
    print(f'{i}:{student[i]}')


"""Dostup k znacheniam slovara"""

# print(student)
# print(type(student['name']))
# print(type(student['age']))
# print(type(student.get('nam','ключ не найден')))
#
# print(type(student))



