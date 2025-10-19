def get_office_sequence(tpl, element):
    if element not in tpl:
        return ()
    first_index = tpl.index(element)
    try:
        second_index = tpl.index(element, first_index + 1)
        return tpl[first_index:second_index + 1]
    except ValueError:
        return tpl[first_index:]
test_cases = [
    ((1, 2, 3), 8),
    ((1, 8, 3, 4, 8, 8, 9, 2), 8),
    ((1, 2, 8, 5, 1, 2, 9), 8)
]
for i, (tpl, elem) in enumerate(test_cases, 1):
    result = get_office_sequence(tpl, elem)
    print(f"Тест {i}:")
    print(f"Входные данные: {tpl}, {elem}")
    print(f"Результат: {result}")
    print()
