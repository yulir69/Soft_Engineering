class NegativeNumberError(Exception):
    pass

def check_positive(number):

    if number < 0:
        raise NegativeNumberError(f"Число {number} отрицательное! Ожидалось положительное.")
    print(f"Число {number} положительное ✓")

def calculate_square_root(number):
    try:
        if number < 0:
            raise NegativeNumberError(f"Нельзя извлечь корень из отрицательного числа: {number}")
        result = number ** 0.5
        print(f"Квадратный корень из {number} = {result:.2f}")
    except NegativeNumberError as e:
        print(e)
check_positive(5)
check_positive(-3)

calculate_square_root(16)
calculate_square_root(-9)