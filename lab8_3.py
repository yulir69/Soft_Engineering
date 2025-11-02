# Базовый класс Car (автомобиль)
class Car:
    # Конструктор базового класса
    def __init__(self, make, model):
        self.make = make
        self.model = model

    # Метод для движения автомобиля
    def drive(self):
        print(f"Driving the {self.make} {self.model}")


# Класс ElectricCar наследуется от класса Car
# Использует все методы и атрибуты родительского класса
class ElectricCar(Car):
    # Конструктор класса ElectricCar
    # Принимает дополнительный параметр battery_capacity (емкость батареи)
    def __init__(self, make, model, battery_capacity):
        # Вызываем конструктор родительского класса Car
        # super() - обращение к родительскому классу
        super().__init__(make, model)
        # Добавляем новый атрибут - емкость батареи
        self.battery_capacity = battery_capacity

    # Новый метод для зарядки электромобиля
    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")


# Создаем объект класса ElectricCar
my_electric_car = ElectricCar("Tesla", "Model S", 75)

# Машина едет (используется унаследованный метод drive)
my_electric_car.drive()

# Машина заряжается (используется новый метод charge)
my_electric_car.charge()
