def safe_execution(func):
    def wrapper(*args, **kwargs):
        try:
            for arg in args:
                if not isinstance(arg, int):
                    raise TypeError(f"Аргумент {arg} должен быть integer")
            for key, value in kwargs.items():
                if not isinstance(value, int):
                    raise TypeError(f"Аргумент {key}={value} должен быть integer")
            result = func(*args, **kwargs)
            print("Программа успешно выполнена")
            return result
        except Exception as e:
            print(f"Выявлена ошибка: {e}")
        finally:
            print("Завершение работы функции")

    return wrapper

@safe_execution
def process_data(x, y):
    return x + y
process_data(10, 20)
process_data(10, "строка")