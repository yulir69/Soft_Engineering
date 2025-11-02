# Определяем класс Car (автомобиль)
class Car:
    # Конструктор класса - инициализирует объект при создании
    def __init__(self, make, model):
        # Атрибут производителя автомобиля
        self.make = make
        # Атрибут модели автомобиля
        self.model = model

    # Метод для "движения" автомобиля
    # Информация о состоянии "машина едет"
    def drive(self):
        print(f"Driving the {self.make} {self.model}")

# Создаем объект класса Car
my_car = Car("Toyota", "Corolla")

# Вызываем метод drive() для объекта my_car
# Машина "поедет" - выведется сообщение в консоль
my_car.drive()
