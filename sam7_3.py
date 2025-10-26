with open("input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

letter_count = sum(len([ch for ch in line if ch.isalpha()]) for line in lines)
word_count = sum(len(line.split()) for line in lines)
line_count = len(lines)

print("Входной файл содержит:")
print(f"{letter_count} букв")
print(f"{word_count} слов")
print(f"{line_count} строк")