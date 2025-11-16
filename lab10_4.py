class NameTooLongError(Exception):
    pass
def validate_name_length(func):
    def wrapper(name, *args, **kwargs):
        if len(name) > 10:
            raise NameTooLongError(f"Имя '{name}' слишком длинное (максимум 10 символов)")
        else:
            print("Успешная регистрация")
            return func(name, *args, **kwargs)
    return wrapper

@validate_name_length
def register_name(name):
    print(f"Имя '{name}' принято")

register_name("Александр")
register_name("Иван")