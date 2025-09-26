import sqlite3
# A4
connect = sqlite3.connect("users.db")
# Рука с ручкой
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    name VARCAHR (100) NOT NULL,
    age INTEGER NOT NULL,
    hobby TEXT
    )
''')
connect.commit()


# CRUD = Create - Read - Update - Delete

def add_user(name_1, age, hobby):
   # cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES("{name}", "{age}", "{hobby}")')
   cursor.execute(
       "INSERT INTO users(name, age, hobby) VALUES(?,?,?)",
       (name_1, age, hobby)

   )
   connect.commit()
print('Пользователь добавлен!!')

# add_user("oleg", 26, "храпеть!!")

def get_users():
    cursor.execute('SELECT name, age, hobby FROM users')
    users = cursor.fetchall()
    #users = cursor.fetchone()
    #users = cursor.fetchmany(2)
    for user in users:
        print(f'name:{user[0]} age:{user[1]} hobby:{user[2]}')

# get_users()

def update_user(name, row_id):
     cursor.execute(
         'UPDATE users SET name = ? WHERE rowid = ?',
         (name, row_id)
     )
     connect.commit()
     print('Пользователь обновлен!!')

update_user("Arzybek", 2)

get_users()

def delete_user(row_id):
    cursor.execute(f'DELETE FROM users WHERE rowid = {row_id}')
    connect.commit()
    print('Пользователь удален!!')
delete_user(2  )