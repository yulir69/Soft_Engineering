class Logger:
    def __init__(self, func):
        print('> Класс Logger метод __init__ успешный запуск')
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'> Проверка перед запуском {self.func.__name__}')
        result = self.func(*args, **kwargs)
        print('> Проверка безопасного выключения')
        return result

@Logger
def site():
    print('Усердная работа сайта')

if __name__ == '__main__':
    print('>> Сайт запущен')
    site()
    print('>> Сайт выключен')