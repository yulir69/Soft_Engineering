def load_forbidden_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            return content.split()
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return []
def censor_text(text, forbidden_words):
    result = text
    for word in forbidden_words:
        start = 0
        while True:
            index = result.lower().find(word.lower(), start)
            if index == -1:
                break
            original_word = result[index:index + len(word)]
            stars = '*' * len(original_word)
            result = result[:index] + stars + result[index + len(word):]
            start = index + len(stars)
    return result
def show_tasks():
    try:
        with open('tasks.txt', 'r', encoding='utf-8') as file:
            tasks = file.readlines()
            if not tasks:
                print("Список дел пуст!")
            else:
                print("\n--- Мой список дел ---")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("Список дел пуст!")
def add_task():
    task = input("Введите новую задачу: ")
    with open('tasks.txt', 'a', encoding='utf-8') as file:
        file.write(task + '\n')
    print("Задача добавлена!")
def clear_tasks():
    confirm = input("Вы уверены, что хотите очистить весь список? (да/нет): ")
    if confirm.lower() == 'да':
        with open('tasks.txt', 'w', encoding='utf-8') as file:
            pass
        print("Список очищен!")
    else:
        print("Очистка отменена.")
def main():
    while True:
        print("\n=== Меню списка дел ===")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Очистить список")
        print("4. Выйти")
        choice = input("Выберите действие (1-4): ")
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            clear_tasks()
        elif choice == '4':
            print("До свидания!")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")
if __name__ == "__main__":
    main()