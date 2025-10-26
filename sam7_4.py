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


def main():
    forbidden_words = load_forbidden_words('input.txt')

    test_text = """Hello, world! Python IS the programming language of thE future. 
My EMAIL is....
PYTHON is awesome!!!!"""

    censored_text = censor_text(test_text, forbidden_words)

    print(censored_text)


if __name__ == "__main__":
    main()