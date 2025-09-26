import sqlite3

# ----------------------
# Шаг 1: Создание базы и таблицы
# ----------------------
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    grade INTEGER,
    subject TEXT
)
""")
conn.commit()

# ----------------------
# Шаг 2: CRUD функции
# ----------------------

def add_student(first_name, last_name, grade, subject):
    cursor.execute("INSERT INTO students (first_name, last_name, grade, subject) VALUES (?, ?, ?, ?)",
                   (first_name, last_name, grade, subject))
    conn.commit()
    print(f"Студент {first_name} {last_name} добавлен!")

def get_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    if students:
        for s in students:
            print(s)
    else:
        print("Студентов нет.")

def update_student(student_id, new_first_name, new_last_name):
    cursor.execute("UPDATE students SET first_name = ?, last_name = ? WHERE id = ?",
                   (new_first_name, new_last_name, student_id))
    conn.commit()
    print(f"Студент с ID {student_id} обновлен!")

def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print(f"Студент с ID {student_id} удален!")

# ----------------------
# Шаг 3: Тестирование
# ----------------------

# Добавляем студентов
add_student("Иван", "Иванов", 10, "Математика")
add_student("Мария", "Петрова", 9, "Физика")
add_student("Алексей", "Сидоров", 11, "Информатика")

print("\nВсе студенты:")
get_students()

# Обновим студента
update_student(2, "Марина", "Петровская")

print("\nПосле обновления студента с ID 2:")
get_students()

# Удалим студента
delete_student(1)

print("\nПосле удаления студента с ID 1:")
get_students()

# Закрываем соединение
conn.close()
