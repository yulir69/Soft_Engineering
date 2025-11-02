# Базовый (общий) класс Shape (фигура)
class Shape:
    # Базовый метод для вычисления площади
    # В базовом классе этот метод возвращает 0 (заглушка)
    def area(self):
        return 0.0
# Класс Rectangle (прямоугольник) наследуется от Shape
class Rectangle(Shape):
    # Конструктор принимает ширину и высоту
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # Переопределяем метод area для прямоугольника
    # Площадь прямоугольника = ширина * высота
    def area(self):
        return self.width * self.height
# Класс Circle (круг) наследуется от Shape
class Circle(Shape):
    # Конструктор принимает радиус
    def __init__(self, radius):
        self.radius = radius
    # Переопределяем метод area для круга
    # Площадь круга = π * радиус²
    def area(self):
        pi = 3.14
        return pi * self.radius * self.radius
# Создаем массив с фигурами
shapes = [
    Rectangle(5, 10),    # Прямоугольник 5x10
    Circle(3)            # Круг с радиусом 3
]

# Проходим по массиву и выводим площади фигур
# Полиморфизм: метод area() вызывается для разных типов объектов
for shape in shapes:
    print(shape.area())
