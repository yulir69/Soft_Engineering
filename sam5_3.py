import math
one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

print("Исходные списки:")
print(f"one = {one}")
print(f"two = {two}")
print(f"three = {three}")
print()

min_a = min(one)
min_b = min(two)
min_c = min(three)

max_a = max(one)
max_b = max(two)
max_c = max(three)

print("Минимальные элементы:")
print(f"min(one) = {min_a}, min(two) = {min_b}, min(three) = {min_c}")
print("Максимальные элементы:")
print(f"max(one) = {max_a}, max(two) = {max_b}, max(three) = {max_c}")
print()

def calculate_triangle_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return area
    else:
        return None
area_min = calculate_triangle_area(min_a, min_b, min_c)
area_max = calculate_triangle_area(max_a, max_b, max_c)
print("РЕЗУЛЬТАТЫ:")
if area_min is not None:
    print(f"Площадь треугольника из минимальных элементов ({min_a}, {min_b}, {min_c}): {area_min:.2f}")
else:
    print(f"Из минимальных элементов ({min_a}, {min_b}, {min_c}) нельзя составить треугольник")

if area_max is not None:
    print(f"Площадь треугольника из максимальных элементов ({max_a}, {max_b}, {max_c}): {area_max:.2f}")
else:
    print(f"Из максимальных элементов ({max_a}, {max_b}, {max_c}) нельзя составить треугольник")