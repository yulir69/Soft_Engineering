# 1. Создание класса и объекта
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"


# Создание объекта
car1 = Car("BMW", "X5", 2022)
print("Создание класса и объекта:")
print(car1.display_info())
print()


# 2. Добавление атрибутов и методов
class Car:
    def __init__(self, brand, model, year, color, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.mileage = 0

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}, цвет: {self.color}"

    def drive(self, distance):
        self.mileage += distance
        return f"Проехали {distance} км. Общий пробег: {self.mileage} км"

    def get_price(self):
        return f"Цена: ${self.price}"


# Создание объекта с новыми атрибутами
car2 = Car("Honda", "Civic", 2023, "синий", 25000)
print("Добавление атрибутов и методов:")
print(car2.display_info())
print(car2.get_price())
print(car2.drive(150))
print()


# 3. Реализация наследования
class ElectricCar(Car):
    def __init__(self, brand, model, year, color, price, battery_capacity):
        super().__init__(brand, model, year, color, price)
        self.battery_capacity = battery_capacity  # в кВт·ч
        self.charge_level = 100  # в процентах

    def charge(self, percent):
        self.charge_level = min(100, self.charge_level + percent)
        return f"Зарядка на {percent}%. Текущий заряд: {self.charge_level}%"

    def display_info(self):
        return f"{super().display_info()}, батарея: {self.battery_capacity} кВт·ч"


# Создание объекта класса-наследника
electric_car = ElectricCar("Tesla", "Model 3", 2024, "белый", 45000, 75)
print("Реализация наследования:")
print(electric_car.display_info())
print(electric_car.charge(30))
print(electric_car.drive(200))
print()


# 4. Реализация инкапсуляции
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance  # приватный атрибут

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"внесено ${amount}. Новый баланс: ${self.__balance}"
        return "сумма должна быть положительной"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"снято ${amount}. Новый баланс: ${self.__balance}"
        return "недостаточно средств или неверная сумма"

    def get_balance(self):
        return f"Баланс счета: ${self.__balance}"

    # Публичный метод для доступа к приватному атрибуту
    def check_balance(self):
        return self.__balance


# Создание объекта с инкапсуляцией
account = BankAccount("Иван Иванов", 1000)
print("Реализация инкапсуляции:")
print(account.get_balance())
print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(2000))  # попытка снять больше чем есть
print()

# 5. Реализация полиморфизма
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return f"{self.name} говорит: Гав-гав!"


class Cat(Animal):
    def make_sound(self):
        return f"{self.name} говорит: Мяу-мяу!"


class Cow(Animal):
    def make_sound(self):
        return f"{self.name} говорит: Му-у-у!"


# Демонстрация полиморфизма
def animal_concert(animals):
    for animal in animals:
        print(animal.make_sound())


# Создание объектов разных классов
animals = [
    Dog("Бобик"),
    Cat("Мурка"),
    Cow("Зорька")
]

print("Реализация полиморфизма:")
animal_concert(animals)