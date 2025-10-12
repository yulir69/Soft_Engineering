def improve_grades(grades):
    improved = []
    for grade in grades:
        if grade == 2:
            continue
        elif grade == 3:
            improved.append(4)
        else:
            improved.append(grade)
    return improved

grades_list_1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades_list_2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades_list_3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

print("\n1) Первый список оценок:")
print(f"Исходные оценки: {grades_list_1}")
improved_1 = improve_grades(grades_list_1)
print(f"Улучшенные оценки: {improved_1}")
print(f"Статистика: было {len(grades_list_1)} оценок, стало {len(improved_1)} оценок")
print(f"Удалено двоек: {grades_list_1.count(2)}, заменено троек: {grades_list_1.count(3)}")

print("\n2) Второй список оценок:")
print(f"Исходные оценки: {grades_list_2}")
improved_2 = improve_grades(grades_list_2)
print(f"Улучшенные оценки: {improved_2}")
print(f"Статистика: было {len(grades_list_2)} оценок, стало {len(improved_2)} оценок")
print(f"Удалено двоек: {grades_list_2.count(2)}, заменено троек: {grades_list_2.count(3)}")

print("\n3) Третий список оценок:")
print(f"Исходные оценки: {grades_list_3}")
improved_3 = improve_grades(grades_list_3)
print(f"Улучшенные оценки: {improved_3}")
print(f"Статистика: было {len(grades_list_3)} оценок, стало {len(improved_3)} оценок")
print(f"Удалено двоек: {grades_list_3.count(2)}, заменено троек: {grades_list_3.count(3)}")
