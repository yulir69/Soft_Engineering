from triangle import triangle_area

a = float(input("Сторона a: "))
b = float(input("Сторона b: "))
c = float(input("Сторона c: "))

area = triangle_area(a, b, c)
print(f"Площадь треугольника: {area}")