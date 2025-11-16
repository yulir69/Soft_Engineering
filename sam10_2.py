def check_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content.strip():
                raise Exception("файл пустой")
            print("Содержимое файла:")
            print(content)
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print(e)

check_file("empty.txt")
check_file("data.txt")