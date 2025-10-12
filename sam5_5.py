def create_special_set(numbers):
    from collections import Counter
    count_dict = Counter(numbers)
    result_set = set()

    for num, count in count_dict.items():
        result_set.add(num)
        for i in range(2, count + 1):
            result_set.add(str(num) * i)

    return result_set
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
print("\n1) Первый список:")
print(f"Исходный список: {list_1}")
set_1 = create_special_set(list_1)
print(f"Результирующее множество: {set_1}")

print("\n2) Второй список:")
print(f"Исходный список: {list_2}")
set_2 = create_special_set(list_2)
print(f"Результирующее множество: {set_2}")

print("\n3) Третий список:")
print(f"Исходный список: {list_3}")
set_3 = create_special_set(list_3)
print(f"Результирующее множество: {set_3}")
