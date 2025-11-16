def add_two():
    try:
        number = input("Введите число: ")
        number = float(number)
        result = 2 + number
        print(f"Результат: 2 + {number} = {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

add_two()
add_two()
add_two()
