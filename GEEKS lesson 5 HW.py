data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

designations = []
codes = []

for i in data:
    if i.isdigit():
        codes.append(i)
    else:
        designations.append(i)

operators = dict(zip(designations, codes))
operators.pop('Katel')
operators.pop('Fonex')

operators['O!'] = {'0702', '0705', '0706'}
operators['Megacom'] = {'0550', '0502', '0552'}
operators['Beeline'] = {'0770', '0575', '3535'}

for key, value in operators.items():
    print(f'{key} - {value}')
