def age_validator(func):
    def wrapper(*args, **kwargs):
        if len(args) >= 2:
            name, age = args[0], args[1]
        else:
            name = kwargs.get('name', '')
            age = kwargs.get('age', 0)

        if not (0 < age < 130):
            raise ValueError("Возраст должен быть больше 0 и меньше 130")

        return func(*args, **kwargs)
    return wrapper

@age_validator
def register_user(name, age):
    print(f"Пользователь {name}, возраст {age} успешно зарегистрирован")

register_user("Илья", 25)
register_user("Мария", 150)