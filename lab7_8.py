import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} Содержит: ')
    print(f'Директорies: {"," .join([folder for folder in catalog[1]])}')
    print(f'Файles: {"," .join([file for file in catalog[2]])}')

print_docs('C:/Users/Hp/OneDrive/Рабочий стол/pe/theme3')
