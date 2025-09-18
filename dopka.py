geektech = {
   'name': 'Geektech',
    'address': "Токтогула 175",
    'courses': {'Backend', 'Android'}
}

geeks = dict(name="GEEKS", address="Ибраимова 103")
geektech.update(geeks)
geeks = geektech.copy()
geeks['courses'].update(['Frontend', ios'])
print(geeks)

# 1) ("name': 'GEEKS', 'address': "Ибраимова 103 courses': ('ios', 'Frontend", "Backend Android
# 14 2) ('name': 'Geektech', 'address': 'Ибраимова 103', 'courses': ('Frontend', 'Backend', 'Android'']
# 15
# 3) Ошибка
# 16 4) [('name',
# 'GEEKS' ), ('address', "Токтогула 175'), ("courses', ('Backend", "ios', "Android'))]
