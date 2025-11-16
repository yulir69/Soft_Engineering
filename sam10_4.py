class Colorizer:
    def __init__(self, color):
        self.color = color
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            colors = {
                'red': '\033[91m',
                'green': '\033[92m',
                'blue': '\033[94m',
                'end': '\033[0m'
            }
            print(f"{colors.get(self.color, '')}", end='')
            result = func(*args, **kwargs)
            print(f"{colors['end']}", end='')
            return result
        return wrapper
@Colorizer('green')
def say_hello(name):
    print(f"Привет, {name}!")
@Colorizer('red')
def say_bye(name):
    print(f"Пока, {name}!")
say_hello("Анна")
say_bye("Иван")