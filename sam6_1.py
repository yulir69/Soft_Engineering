input_data = input("Введите последовательность чисел, разделенных пробелом: ")
numbers_list = input_data.split()
numbers_list = [int(num) for num in numbers_list]
numbers_tuple = tuple(numbers_list)

print("Список:", numbers_list)
print("Кортеж:", numbers_tuple)