checks = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365, 1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444, 5556, 6666, 5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928, 5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987, 3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506]
total_checks = len(checks)
unique_people = len(set(checks))
from collections import Counter
visits_count = Counter(checks)
most_frequent_worker, max_visits = visits_count.most_common(1)[0]

print("результаты анализа посещений ресторана за неделю:")
print(f"всего выдано чеков: {total_checks}")
print(f"разных людей посетило ресторан: {unique_people}")
print(f"сотрудник с кодом {most_frequent_worker} посетил ресторан больше всех раз: {max_visits} раз(а)")
print("\nтоп 5 самых частых посетителей:")
for worker, count in visits_count.most_common(5):
    print(f"код сотрудника: {worker}, посещений: {count}")