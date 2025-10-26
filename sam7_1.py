from collections import Counter
import re

with open("statia.txt", "r", encoding="utf-8") as file:
    text = file.read()

words = re.findall(r'\b\w+\b', text.lower())
word_count = len(words)
most_common_word, count = Counter(words).most_common(1)[0]

print(f"Общее количество слов: {word_count} ")
print(f"Самое частое слово: '{most_common_word}' (встречается {count} раз)")