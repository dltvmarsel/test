import string

def is_strong_password(password: str) -> bool:
    if len(password) < 6:
        print('Этот пароль слишком лёгкий, попробуй ещё')
        return False
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    if not (has_lower and has_upper and has_digit):
        print('Пароль должен содержать цифры, строчные и заглавные буквы')
        return False
    specials_count = sum(c in string.punctuation for c in password)
    if specials_count < 2:
        print('Пароль должен содержать как минимум 2 спецсимвола')
        return False
    print("Надёжный пароль, молодец")
    return True

while True:
    user_password = input("Введите пароль: ")
    if is_strong_password(user_password):
        break
