def count_digits(sequence):
    digit_count = {}
    for char in sequence:
        if char.isdigit():
            digit = int(char)
            digit_count[digit] = digit_count.get(digit, 0) + 1
    sorted_digits = sorted(digit_count.items(), key=lambda x: (-x[1], x[0]))
    top_three = sorted_digits[:3]
    top_three_sorted = sorted(top_three, key=lambda x: x[0])
    result_dict = dict(top_three)
    print("Топ-3 самых часто встречаемых чисел (в порядке возрастания ключа):")
    for digit, count in top_three_sorted:
        print(f"Цифра {digit}: {count} раз(а)")
    return result_dict
def main():
    test_sequence = "123456789012345678901234567890"
    if len(test_sequence) < 15:
        print("Строка слишком короткая! Минимум 15 символов.")
        return
    print(f"Исходная последовательность: {test_sequence}")
    print(f"Длина последовательности: {len(test_sequence)} символов")
    result = count_digits(test_sequence)
    print("Словарь с топ-3 самыми частыми цифрами:")
    print(result)
def additional_tests():
    test_cases = [
        "111222333444555666777",
        "123123123456456456789",
        "000111222333444555666",
    ]
    for i, sequence in enumerate(test_cases, 1):
        print(f"\nТест {i}:")
        print(f"Последовательность: {sequence}")
        result = count_digits(sequence)
        print(f"Результат: {result}")
if __name__ == "__main__":
    main()
    additional_tests()