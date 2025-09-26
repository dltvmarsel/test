# Импортируем библиотеку Pandas
import pandas as pd

# === Чтение CSV файла ===
# Замените 'вашфайл.csv' на ваш настоящий файл
# df = pd.read_csv('вашфайл.csv')

# === Отображение DataFrame ===
# Первые 5 строк
# df.head()

# Последние 5 строк
# df.tail()

# Весь DataFrame (осторожно, если он большой)
# print(df)

# === Выбор колонок ===
# Одна колонка
# df['column_name']

# Несколько колонок
# df[['column_1', 'column_2']]

# === Фильтрация строк ===
# Все строки, где age > 30
# df[df['age'] > 30]

# === Сортировка ===
# По возрасту (по возрастанию)
# df.sort_values(by='age')

# По возрасту (по убыванию)
# df.sort_values(by='age', ascending=False)

# === Группировка ===
# Среднее значение по колонке gender
# df.groupby('gender').mean()

# === Джойны (объединение DataFrame) ===
# df1 = pd.read_csv('вашфайл1.csv')
 df2 = pd.read_csv('вашфайл2.csv')
 df1.merge(df2, on='user_id')

=== Сводные таблицы (Pivot) ===
df.pivot_table(index='gender', columns='age', values='column_name', aggfunc='mean')
