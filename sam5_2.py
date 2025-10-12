results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
sorted_results = sorted(results)

print("Анализ результатов бега:")
print(f"Все результаты: {results}")
print()

print("Три лучших результата:")
best_results = sorted_results[:3]
for i, result in enumerate(best_results, 1):
    print(f"{i} место: {result} сек")
print()

print("Три худшие результата:")
worst_results = sorted_results[-3:]
for i, result in enumerate(worst_results[::-1], 1):
    print(f"{i} место с конца: {result} сек")

print()

print("Все результаты начиная с 10-го:")
results_from_10th = sorted_results[9:]
for i, result in enumerate(results_from_10th, 10):
    print(f"{i} результат: {result} сек")

print()
