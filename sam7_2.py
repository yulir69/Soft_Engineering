def add_expense():
    amount = input("Введите сумму расхода: ")
    category = input("Введите категорию расхода: ")
    with open("rashod.txt", "a", encoding="utf-8") as file:
        file.write(f"{amount} {category}\n")

def show_expenses():
    try:
        with open("rashod.txt", "r", encoding="utf-8") as file:
            print("История расходов:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Файл с расходами пуст.")

while True:
    action = input("1 - Добавить расход, 2 - Показать расходы, 3 - Выход: ")
    if action == "1":
        add_expense()
    elif action == "2":
        show_expenses()
    elif action == "3":
        break