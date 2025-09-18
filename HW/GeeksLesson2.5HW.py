def check_admin(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if role == "админ":
                return func(*args, **kwargs)
            else:
                print("Доступ запрещён")
        return wrapper
    return decorator


@check_admin("арзы")
def delete_user():
    print("Пользователь удалён")


@check_admin("админ")
def add_user():
    print("Пользователь добавлен")


delete_user()
add_user()
